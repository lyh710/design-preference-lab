"""Loopback-only development server; no external services or hosted deployment."""

import json
import sqlite3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from .store import Store

STATIC = Path(__file__).parent / "static"
MAX_BODY = 16384


def make_server(port: int, db_path: Path) -> ThreadingHTTPServer:
    store = Store(db_path)

    class Handler(BaseHTTPRequestHandler):
        server: ThreadingHTTPServer

        def log_message(self, format: str, *args: Any) -> None:
            pass

        def send(self, status: int, body: bytes, content_type: str) -> None:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header(
                "Content-Security-Policy",
                "default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self'; frame-ancestors 'none'; base-uri 'none'",
            )
            self.end_headers()
            self.wfile.write(body)

        def json_response(self, status: int, value: Any) -> None:
            self.send(
                status,
                json.dumps(value, ensure_ascii=True).encode(),
                "application/json; charset=utf-8",
            )

        def trusted_host(self) -> bool:
            host = self.headers.get("Host", "")
            port = self.server.server_port
            return host in (f"127.0.0.1:{port}", f"localhost:{port}")

        def do_GET(self) -> None:
            if not self.trusted_host():
                self.json_response(403, {"error": "Use the local app address."})
                return
            path = urlsplit(self.path).path
            try:
                if path == "/api/export":
                    self.json_response(200, store.export())
                elif path.startswith("/api/comparisons/"):
                    self.json_response(200, store.get(path.rsplit("/", 1)[-1]))
                elif path in ("/", "/app.js", "/style.css"):
                    name, content_type = {
                        "/": ("index.html", "text/html"),
                        "/app.js": ("app.js", "text/javascript"),
                        "/style.css": ("style.css", "text/css"),
                    }[path]
                    self.send(200, (STATIC / name).read_bytes(), content_type + "; charset=utf-8")
                else:
                    self.json_response(404, {"error": "Not found."})
            except KeyError:
                self.json_response(404, {"error": "Comparison not found."})
            except sqlite3.Error:
                self.json_response(503, {"error": "Local storage is unavailable. Please retry."})

        def do_POST(self) -> None:
            host = self.headers.get("Host", "")
            origin = self.headers.get("Origin")
            if (
                not self.trusted_host()
                or (origin is not None and origin != f"http://{host}")
                or self.headers.get("Sec-Fetch-Site") == "cross-site"
            ):
                self.json_response(403, {"error": "Requests must come from the local app."})
                return
            if self.headers.get("Content-Type", "").split(";")[0] != "application/json":
                self.json_response(415, {"error": "Send application/json."})
                return
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= MAX_BODY:
                    self.json_response(413, {"error": "Request must contain 1–16384 bytes."})
                    return
                payload = json.loads(self.rfile.read(length))
                if not isinstance(payload, dict):
                    raise ValueError("Expected a JSON object.")
                path = urlsplit(self.path).path
                if path == "/api/comparisons":
                    self.json_response(
                        201, store.create(payload.get("brief"), payload.get("seed", 42))
                    )
                elif path == "/api/preferences":
                    self.json_response(
                        200,
                        store.vote(
                            payload.get("id"), payload.get("choice"), payload.get("reason", "")
                        ),
                    )
                else:
                    self.json_response(404, {"error": "Not found."})
            except (ValueError, UnicodeError) as error:
                self.json_response(400, {"error": str(error)})
            except KeyError:
                self.json_response(404, {"error": "Comparison not found."})
            except sqlite3.Error:
                self.json_response(503, {"error": "Could not save to local storage. Please retry."})

    return ThreadingHTTPServer(("127.0.0.1", port), Handler)
