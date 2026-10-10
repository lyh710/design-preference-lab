import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class CliTests(unittest.TestCase):
    def test_demo_reproduces_ten_svg_files_and_manifest(self):
        with tempfile.TemporaryDirectory() as temp:
            paths = [Path(temp) / "first", Path(temp) / "second"]
            for path in paths:
                result = subprocess.run(
                    [sys.executable, "-m", "design_lab", "demo", "--output", str(path)],
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(len(list(path.glob("*.svg"))), 10)
                manifest = json.loads((path / "manifest.json").read_text())
                self.assertEqual(len(manifest["comparisons"]), 5)
                self.assertEqual(manifest["generator"], "templates-v1")
            first = {p.name: p.read_bytes() for p in paths[0].iterdir()}
            second = {p.name: p.read_bytes() for p in paths[1].iterdir()}
            self.assertEqual(first, second)
