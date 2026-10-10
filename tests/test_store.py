import tempfile
import unittest
from pathlib import Path

from design_lab.store import Store
from test_core import BRIEF


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / "records.sqlite"
        self.store = Store(self.path)

    def test_blinding_vote_order_and_restart(self):
        record = self.store.create(BRIEF, 42)
        self.assertNotIn("metrics", record["designs"][0])
        self.assertNotIn("variant", record["designs"][0])
        left_id = record["designs"][0]["id"]
        voted = self.store.vote(record["id"], "left", "The title stands out.")
        self.assertEqual(voted["preference"]["winner_id"], left_id)
        self.assertIn("metrics", voted["designs"][0])
        self.assertEqual(Store(self.path).get(record["id"]), voted)
        self.assertEqual(self.store.export()["comparisons"], [voted])

    def test_rejects_duplicate_invalid_and_unknown_votes(self):
        record = self.store.create(BRIEF, 1)
        with self.assertRaises(ValueError):
            self.store.vote(record["id"], "third", "")
        with self.assertRaises(ValueError):
            self.store.vote(record["id"], "left", "a" * 1001)
        with self.assertRaises(KeyError):
            self.store.vote("missing", "left", "")
        self.assertIsNone(self.store.get(record["id"])["preference"])
        self.store.vote(record["id"], "neither", "")
        with self.assertRaises(ValueError):
            self.store.vote(record["id"], "right", "")
        self.assertIsNone(self.store.get(record["id"])["preference"]["winner_id"])

    def test_export_preserves_blinding_for_unrated_pairs(self):
        self.store.create(BRIEF, 2)
        self.assertNotIn("metrics", self.store.export()["comparisons"][0]["designs"][0])

    def test_invalid_unicode_reason_is_rejected_before_saving(self):
        record = self.store.create(BRIEF, 3)
        with self.assertRaisesRegex(ValueError, "unsupported Unicode"):
            self.store.vote(record["id"], "left", chr(0xD800))
        self.assertIsNone(self.store.get(record["id"])["preference"])
