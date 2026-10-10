# Lesson 01 — what does the generator learn?

**Purpose:** connect the working poster app to the first real training loop.
Allow 15–20 minutes. Current progress belongs in [learning-state.md](../learning-state.md).

Today the app follows handwritten layout rules. In the proposed exercise, a small
model will see a brief and learn to predict the layout text. This develops the
training skill in our [role brief](../role-context.md); matching a template does
not establish that a model understands good design.

## One input and one target

The input contains an instruction and this first fictional brief from
[briefs.json](../../design_lab/examples/briefs.json):

```json
{"title":"Tomorrow, together","details":"A community design evening · 18 October · Harbour Hall","cta":"Reserve your place"}
```

For the first exercise, use the same instruction every time: “Return the layout
JSON for this brief using the fixed teaching template.” Fix seed 0 and variant 0
when making teaching examples. Otherwise the same input could have different
targets because of a colour or template choice the input never specifies.

This is the target, taken from `generate_pair(brief, seed=0)[0]` in
[core.py](../../design_lab/core.py), keeping only the fields needed by the renderer:

```json
{
  "width":600,"height":800,"background":"#29223d","accent":"#fbbca6",
  "elements":[
    {"role":"title","text":"Tomorrow, together","x":48,"y":145,"width":504,"height":210,"font_size":54,"color":"#fff4e4"},
    {"role":"details","text":"A community design evening · 18 October · Harbour Hall","x":48,"y":405,"width":504,"height":120,"font_size":23,"color":"#fff4e4"},
    {"role":"cta","text":"Reserve your place","x":48,"y":660,"width":504,"height":80,"font_size":24,"color":"#fbbca6"}
  ]
}
```

The model predicts layout text, not SVG pixels or a preference score. The existing
renderer turns the layout into a poster. IDs, seed, generator version and the
duplicated brief remain experiment metadata, outside the prediction target.

Reproduce the example from the repository root; this does not train anything:

```sh
python3 - <<'PY'
import json
from pathlib import Path
from design_lab.core import generate_pair, render_svg, stable_json

brief = json.loads(Path("design_lab/examples/briefs.json").read_text())[0]
design = generate_pair(brief, seed=0)[0]
target = {key: design[key] for key in ("width", "height", "background", "accent", "elements")}
assert render_svg(target) == render_svg(design)
print(stable_json(target))
PY
```

The displayed JSON is spaced for reading. Training should use the compact,
consistently ordered representation printed by this command.

## What one training step asks

A token is one piece of the sequence. A tiny model can use individual text bytes;
larger models commonly use pieces of words. Given the instruction, brief and the
correct layout prefix so far, the model predicts the next token. Training compares
that prediction with the next token in the saved target, then adjusts the weights.
At generation time, it receives the brief and its own previous output instead of
the correct target prefix. Small mistakes can therefore accumulate.

**Loss** measures how little probability the model gives the correct next token.
For one token it is `-log(probability of the correct token)`; average over the
tokens we choose to score. A probability of 0.5 gives about 0.69 loss; 0.1 gives
about 2.30. Lower is better at matching these teaching examples.

We will score only the layout completion and its end marker. The instruction,
brief, separator and padding (filler added to equalise sequence lengths) stay out
of the score. They are still available as context. PyTorch can ignore such labels
using `-100`; see its [cross-entropy loss reference](https://docs.pytorch.org/docs/2.14/generated/torch.nn.CrossEntropyLoss.html).

The labels must be shifted by one position: the last prompt token predicts the
first layout token. Inspect that boundary explicitly. For a tiny illustrative
sequence with prompt `P :`, target `{ }`, end marker `END`, and padding `PAD`:

| Input token at this position | Correct next token | Label used for loss |
| --- | --- | --- |
| `P` | `:` | ignored |
| `:` | `{` | `{` — first target token counts |
| `{` | `}` | `}` |
| `}` | `END` | `END` |
| `END` | `PAD` | ignored |

Masking loss is separate from preventing the model from seeing future tokens.
The model must only use the preceding sequence when making each prediction.

## Two questions before building the exercise

1. In your own words, what is supplied to the model, what must it produce, and
   which tokens should affect the loss?
2. Name a likely failure. How could lower loss coexist with an unattractive or
   unusable poster, and what would you inspect beyond loss?

Record the learner's actual answers in the session log. The worked example alone
does not demonstrate understanding. Continue with the
[tiny experiment card](01-tiny-experiment.md) after discussing the answers.
