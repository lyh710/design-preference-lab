"""Run `python -m design_lab` or generate reproducible demonstration artifacts."""

import argparse
import json
import platform
from pathlib import Path

from .core import GENERATOR_VERSION, comparison, stable_json
from .server import make_server


def main() -> None:
    parser = argparse.ArgumentParser(description="Design Preference Lab — local template baseline")
    commands = parser.add_subparsers(dest="command")
    serve = commands.add_parser("serve", help="Open the local comparison app")
    serve.add_argument("--port", type=int, default=8765)
    serve.add_argument("--db", type=Path, default=Path("data/preferences.sqlite"))
    demo = commands.add_parser("demo", help="Write five repeatable example comparisons")
    demo.add_argument("--output", type=Path, default=Path("runs/demo"))
    demo.add_argument("--briefs", type=Path, default=Path(__file__).parent / "examples/briefs.json")
    args = parser.parse_args()
    if args.command == "demo":
        briefs = json.loads(args.briefs.read_text(encoding="utf-8"))
        records = [comparison(brief, 42 + i) for i, brief in enumerate(briefs)]
        args.output.mkdir(parents=True, exist_ok=True)
        for i, record in enumerate(records):
            for j, design in enumerate(record["designs"]):
                (args.output / f"{i + 1:02d}-{j + 1}.svg").write_text(
                    design["svg"], encoding="utf-8"
                )
        manifest = {
            "schema_version": 1,
            "generator": GENERATOR_VERSION,
            "python": platform.python_version(),
            "comparisons": records,
        }
        (args.output / "manifest.json").write_text(stable_json(manifest) + "\n", encoding="utf-8")
        print(f"Wrote {len(records)} template comparisons to {args.output}")
        return
    port = getattr(args, "port", 8765)
    if not 0 <= port <= 65535:
        parser.error("Port must be between 0 and 65535.")
    server = make_server(port, getattr(args, "db", Path("data/preferences.sqlite")))
    print(
        f"Design Preference Lab: http://127.0.0.1:{server.server_port} (Ctrl+C to stop)", flush=True
    )
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
