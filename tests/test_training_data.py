import json
from pathlib import Path
import subprocess
import sys
import unittest

from design_lab.training_data import encode_example
from design_lab.core import generate_pair, stable_json


class TrainingDataTests(unittest.TestCase):
    def test_shift_scores_first_completion_and_end_but_not_prompt(self):
        inputs, labels = encode_example("P:", "{}")
        self.assertEqual(inputs, [80, 58, 123, 125])
        self.assertEqual(labels, [-100, 123, 125, 256])

    def test_padding_adds_no_loss_and_does_not_drop_end_label(self):
        inputs, labels = encode_example("P:", "{}", pad_to=6)
        self.assertEqual(inputs, [80, 58, 123, 125, 257, 257])
        self.assertEqual(labels, [-100, 123, 125, 256, -100, -100])

    def test_unicode_boundary_counts_bytes_instead_of_characters(self):
        inputs, labels = encode_example("é:", "✓")
        self.assertEqual(inputs, [195, 169, 58, 226, 156, 147])
        self.assertEqual(labels, [-100, -100, 226, 156, 147, 256])

    def test_rejects_empty_text_or_padding_that_would_truncate(self):
        for prompt, target in [("", "{}"), ("P:", "")]:
            with self.subTest(prompt=prompt, target=target), self.assertRaises(ValueError):
                encode_example(prompt, target)
        for pad_to in [3, -1, True]:
            with self.subTest(pad_to=pad_to), self.assertRaises(ValueError):
                encode_example("P:", "{}", pad_to=pad_to)

    def test_cli_prepares_real_pairs_with_scored_completion_and_equal_lengths(self):
        result = subprocess.run(
            [sys.executable, "-m", "design_lab.training_data"],
            check=True,
            capture_output=True,
            text=True,
        )
        report = json.loads(result.stdout)
        self.assertEqual(report["batch_size"], 4)
        data = json.loads(Path("docs/lessons/examples/01-training-pairs.json").read_text())
        self.assertEqual((data["seed"], data["variant"]), (0, 0))
        for source, example in zip(data["examples"], report["examples"], strict=True):
            expected = generate_pair(source["brief"], seed=0)[0]
            layout = {
                key: expected[key]
                for key in ("width", "height", "background", "accent", "elements")
            }
            self.assertEqual(source["layout"], layout)
            self.assertEqual(example["completion"], stable_json(layout))
            self.assertEqual(
                example["prompt"],
                data["instruction"] + "\nBrief:\n" + stable_json(source["brief"]) + "\nLayout:\n",
            )
            inputs, labels = example["input_ids"], example["labels"]
            decoded = bytes(token for token in inputs if token != 257).decode("utf-8")
            self.assertEqual(decoded, example["prompt"] + example["completion"])
            boundary = len(example["prompt"].encode("utf-8")) - 1
            self.assertEqual(len(inputs), report["sequence_length"])
            self.assertEqual(len(labels), len(inputs))
            self.assertTrue(all(label == -100 for label in labels[:boundary]))
            self.assertEqual(labels[boundary], 123)  # First completion byte is '{'.
            scored = [label for label in labels if label != -100]
            self.assertEqual(scored[-1], 256)
            self.assertEqual(bytes(scored[:-1]).decode("utf-8"), example["completion"])
            self.assertEqual(example["scored_tokens"], len(scored))
            self.assertEqual(example["padding_tokens"], inputs.count(257))


if __name__ == "__main__":
    unittest.main()
