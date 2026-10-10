# Step 5 — read the code that prepares training inputs

**Learn:** inspect what the model receives and exactly what it is asked to predict.
This step prepares data; it does not construct a model or update weights.

Source: [training_data.py](../../design_lab/training_data.py), especially
`encode_example`. [Tests](../../tests/test_training_data.py) check the boundary,
padding, Unicode and the real four-example input. This code uses only Python's
standard library; the app still has no training-library dependency.

## Read the code

This is the central excerpt from `encode_example`. The complete function also
rejects empty text and padding lengths that would cut off part of the example.

```python
prompt_ids = list(prompt.encode("utf-8"))
completion_ids = list(completion.encode("utf-8"))

sequence = prompt_ids + completion_ids + [END]
labels = [IGNORE] * len(prompt_ids) + completion_ids + [END]

# Each input position predicts the following token, not itself.
input_ids = sequence[:-1]
labels = labels[1:]
```

1. `encode("utf-8")` converts text to bytes, each a number from 0 to 255. Each byte
   is one token for this exercise. An ASCII character uses one byte; other
   characters can use several. Counting characters instead of bytes would put the
   prompt/layout boundary in the wrong place for some text.
2. `sequence` joins the supplied prompt and expected layout, then adds `END=256`.
   The prompt contains the instruction, brief and `Layout:` separator. The end
   marker teaches the model when to stop.
3. `labels` describes the correct answers used to calculate loss. `IGNORE=-100`
   marks answers that should not be scored. The model still receives the prompt
   as input; we only exclude predictions of prompt tokens from the loss.
4. `sequence[:-1]` removes the last token from the input. `labels[1:]` removes the
   first label. This makes each input position predict the **next** token. The
   final prompt token predicts the first layout token, so that first token counts.

The function then adds padding to make the four rows equally long:

```python
padding = pad_to - len(input_ids)
input_ids += [PAD] * padding
labels += [IGNORE] * padding
```

`PAD=257` is filler, outside the byte range. It is not an answer we want the model
to learn, so its label is ignored. A future model needs 258 token IDs (0 through
257). `-100` is a loss-label setting, never a model input token.

These labels are **already shifted**. In the later PyTorch loop, compare each
position's output directly with these labels using `ignore_index=-100`; do not
shift them again. The model must also prevent access to future tokens. Loss
masking alone does not enforce that. The intended recurrent model processes the
sequence in order. The relevant [PyTorch loss reference](https://docs.pytorch.org/docs/2.14/generated/torch.nn.CrossEntropyLoss.html)
explains ignored class labels; our own tests establish the shift and data contract.

## Run and inspect the real example

From the repository root, after [step 4 setup](01-local-setup.md):

```sh
runs/lesson01-env/bin/python -m design_lab.training_data > runs/lesson01-batch.json
```

The command reads the [four saved pairs](examples/01-training-pairs.json). The
output includes each complete prompt/layout, all input IDs and labels, and the
counts. It prints JSON and writes no files itself; the shell saves that output in
the ignored `runs/` folder. You can pass a different pairs-file path as an argument.

Observed on 10 October 2026: four rows, padded to 611 input positions each.

| Example | Prompt bytes | Layout bytes | Scored labels, including END | Padding |
| --- | ---: | ---: | ---: | ---: |
| Make art | 169 | 426 | 427 | 16 |
| Plant seeds | 171 | 428 | 429 | 12 |
| Hear music | 172 | 429 | 430 | 10 |
| Fix things | 177 | 434 | 435 | 0 |

For the first example, these are actual selected positions (counted from zero):

| Position | Input token | Label | Meaning |
| --- | --- | --- | --- |
| 167 | `:` (58) | ignored (-100) | Predicting the prompt's final newline is not scored |
| 168 | newline (10) | `{` (123) | The first layout token is scored |
| 169 | `{` (123) | `"` (34) | Predict the next layout token |
| 594 | `}` (125) | END (256) | Learn to stop after the layout |
| 595 | PAD (257) | ignored (-100) | Filler contributes no loss |

The row contains the correct completion for training. When generating a new
layout later, the model receives only the prompt and then its own generated tokens.

## Why this matters for the target roles

- **Senior Research Scientist — Design Generation:** preparing training data,
  implementing the training objective and diagnosing bugs. A one-position error
  can train a different task while still producing a decreasing loss. Inspecting
  a decoded example and its labels is a practical training-debugging skill.
- **Principal Research Scientist — Evaluations:** checking what a reported score
  actually measures. Including prompt or padding predictions could change the
  average loss without improving the intended layout completion. Even this
  correctly restricted loss measures imitation of targets, not human preference.

These connections follow the recorded [role brief](../role-context.md). This small
exercise supports those skills; it does not establish expertise by itself.

**Learner check:** why does position 168 count toward the loss even though its
input is still part of the prompt? Discuss the answer before advancing to the
model and training loop. Agent-run checks are complete; learner interpretation of
this code has not yet been recorded.
