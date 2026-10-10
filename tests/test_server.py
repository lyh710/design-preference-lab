import json
import tempfile
import threading
import unittest
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from design_lab.server import make_server
from test_core import BRIEF


class ServerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.server = make_server(0, Path(self.tmp.name) / "test.sqlite")
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.base = f"http://127.0.0.1:{self.server.server_port}"

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()
        self.tmp.cleanup()

    def request(self, path, payload=None, headers=None):
        data = json.dumps(payload).encode() if payload is not None else None
        req = Request(
            self.base + path, data=data, headers=headers or {"Content-Type": "application/json"}
        )
        try:
            response = urlopen(req, timeout=3)
        except HTTPError as error:
            response = error
        with response:
            body = response.read()
            return response.status, json.loads(body) if "json" in response.headers.get(
                "Content-Type", ""
            ) else body

    def test_http_round_trip_and_static_page(self):
        for path, expected in [
            ("/", b"Design Preference Lab"),
            ("/app.js", b"/api/preferences"),
            ("/style.css", b"@media"),
        ]:
            status, body = self.request(path)
            self.assertEqual(status, 200)
            self.assertIn(expected, body)
        status, record = self.request("/api/comparisons", {"brief": BRIEF, "seed": 7})
        self.assertEqual(status, 201)
        self.assertNotIn("metrics", record["designs"][0])
        status, vote = self.request(
            "/api/preferences", {"id": record["id"], "choice": "tie", "reason": "Equal clarity"}
        )
        self.assertEqual(status, 200)
        self.assertEqual(vote["preference"]["choice"], "tie")
        self.assertEqual(self.request("/api/comparisons/" + record["id"])[1], vote)
        self.assertEqual(len(self.request("/api/export")[1]["comparisons"]), 1)

    def test_bad_requests_do_not_write(self):
        self.assertEqual(self.request("/api/comparisons", {"brief": BRIEF, "seed": True})[0], 400)
        self.assertEqual(
            self.request("/api/comparisons", [], {"Content-Type": "application/json"})[0], 400
        )
        self.assertEqual(
            self.request(
                "/api/comparisons",
                {"brief": BRIEF},
                {"Content-Type": "application/json", "Origin": "https://example.org"},
            )[0],
            403,
        )
        self.assertEqual(
            self.request("/api/comparisons", {"brief": BRIEF}, {"Content-Type": "text/plain"})[0],
            415,
        )
        self.assertEqual(
            self.request("/api/comparisons", {"brief": {**BRIEF, "title": "a" * 20000}})[0], 413
        )
        self.assertEqual(self.request("/api/export")[1]["comparisons"], [])
        self.assertEqual(self.request("/api/comparisons/missing")[0], 404)
        self.assertEqual(self.request("/../../README.md")[0], 404)
