"""Immutable comparisons and one anonymous preference per comparison."""

import json
import secrets
import sqlite3
import uuid
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .core import comparison, stable_json


class Store:
    def __init__(self, path: Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with closing(sqlite3.connect(self.path)) as db, db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS comparisons (id TEXT PRIMARY KEY, payload TEXT NOT NULL, preference TEXT)"
            )

    def create(self, brief: Any, seed: int) -> dict[str, Any]:
        record = comparison(brief, seed)
        if secrets.randbits(1):
            record["designs"].reverse()
        record.update(id=uuid.uuid4().hex, created_at=datetime.now(timezone.utc).isoformat())
        with closing(sqlite3.connect(self.path)) as db, db:
            db.execute(
                "INSERT INTO comparisons VALUES (?, ?, NULL)", (record["id"], stable_json(record))
            )
        return self.get(record["id"])

    @staticmethod
    def _public(payload: str, preference: str | None) -> dict[str, Any]:
        record = json.loads(payload)
        record["preference"] = json.loads(preference) if preference else None
        if not preference:
            for design in record["designs"]:
                design.pop("metrics")
                design.pop("variant")
        return record

    def get(self, record_id: str) -> dict[str, Any]:
        with closing(sqlite3.connect(self.path)) as db:
            row = db.execute(
                "SELECT payload, preference FROM comparisons WHERE id = ?", (record_id,)
            ).fetchone()
        if row is None:
            raise KeyError("Comparison not found.")
        return self._public(*row)

    def vote(self, record_id: Any, choice: Any, reason: Any) -> dict[str, Any]:
        if (
            not isinstance(record_id, str)
            or not isinstance(choice, str)
            or choice not in ("left", "right", "tie", "neither")
        ):
            raise ValueError("Choose left, right, tie or neither.")
        if not isinstance(reason, str) or len(reason) > 1000:
            raise ValueError("Reason must be text of at most 1000 characters.")
        if any(0xD800 <= ord(character) <= 0xDFFF for character in reason):
            raise ValueError("Reason contains unsupported Unicode characters.")
        with closing(sqlite3.connect(self.path)) as db, db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute(
                "SELECT payload, preference FROM comparisons WHERE id = ?", (record_id,)
            ).fetchone()
            if row is None:
                raise KeyError("Comparison not found.")
            if row[1] is not None:
                raise ValueError("This comparison already has a saved preference.")
            designs = json.loads(row[0])["designs"]
            winner = (
                designs[0 if choice == "left" else 1]["id"] if choice in ("left", "right") else None
            )
            preference = {
                "choice": choice,
                "winner_id": winner,
                "displayed_ids": [d["id"] for d in designs],
                "reason": reason.strip(),
                "recorded_at": datetime.now(timezone.utc).isoformat(),
                "rubric": "communication-v1",
            }
            db.execute(
                "UPDATE comparisons SET preference = ? WHERE id = ?",
                (stable_json(preference), record_id),
            )
        return self.get(record_id)

    def export(self) -> dict[str, Any]:
        with closing(sqlite3.connect(self.path)) as db:
            rows = db.execute(
                "SELECT payload, preference FROM comparisons ORDER BY rowid"
            ).fetchall()
        return {"schema_version": 1, "comparisons": [self._public(*row) for row in rows]}
