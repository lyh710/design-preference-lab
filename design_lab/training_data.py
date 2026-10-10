"""Inspect byte tokens and completion-only labels; no model or training run."""

import argparse
import json
from pathlib import Path

from design_lab.core import stable_json

END = 256
PAD = 257
IGNORE = -100


def encode_example(
    prompt: str, completion: str, pad_to: int | None = None
) -> tuple[list[int], list[int]]:
    """Return input IDs and already-shifted labels for a next-token loss."""
    if not prompt or not completion:
        raise ValueError("Prompt and completion must both contain text.")
    prompt_ids = list(prompt.encode("utf-8"))
    completion_ids = list(completion.encode("utf-8"))

    sequence = prompt_ids + completion_ids + [END]
    labels = [IGNORE] * len(prompt_ids) + completion_ids + [END]

    # Each input position predicts the following token, not itself.
    input_ids = sequence[:-1]
    labels = labels[1:]

    if pad_to is None:
        pad_to = len(input_ids)
    if type(pad_to) is not int or pad_to < len(input_ids):
        raise ValueError("pad_to must be an integer large enough for the whole example.")
    padding = pad_to - len(input_ids)
    input_ids += [PAD] * padding
    labels += [IGNORE] * padding
    return input_ids, labels


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "pairs",
        nargs="?",
        type=Path,
        default=Path("docs/lessons/examples/01-training-pairs.json"),
        help="Saved lesson pairs; default path is relative to the repository root.",
    )
    args = parser.parse_args()
    data = json.loads(args.pairs.read_text(encoding="utf-8"))
    examples = []
    for example in data["examples"]:
        prompt = data["instruction"] + "\nBrief:\n" + stable_json(example["brief"]) + "\nLayout:\n"
        completion = stable_json(example["layout"])
        inputs, _ = encode_example(prompt, completion)
        examples.append((example["id"], prompt, completion, len(inputs)))
    if not examples:
        parser.error("The pairs file must contain at least one example.")
    sequence_length = max(example[3] for example in examples)
    rows = []
    for example_id, prompt, completion, _ in examples:
        inputs, labels = encode_example(prompt, completion, pad_to=sequence_length)
        rows.append(
            {
                "id": example_id,
                "prompt": prompt,
                "completion": completion,
                "input_ids": inputs,
                "labels": labels,
                "scored_tokens": sum(label != IGNORE for label in labels),
                "padding_tokens": inputs.count(PAD),
            }
        )
    print(
        json.dumps(
            {
                "token_encoding": "utf-8 bytes (0-255), END=256, PAD=257; IGNORE=-100",
                "batch_size": len(rows),
                "sequence_length": sequence_length,
                "examples": rows,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
