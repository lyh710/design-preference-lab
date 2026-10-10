# First tiny training experiment

The learner selected local brief-to-layout training from template examples on
10 October 2026. The details below are a proposed run plan to discuss after the
[worked example](01-training-example.md). No training code or run exists yet.

## Step 3 — inspect the four training examples

The [saved training pairs](examples/01-training-pairs.json) contain four fictional
briefs and their exact template layouts. All four are training examples:

| Title | Details | Call to action |
| --- | --- | --- |
| Make art | Art class - Monday at 6 pm | Book a place |
| Plant seeds | Garden club - Tuesday at 10 am | Join us |
| Hear music | Music night - Friday at 7 pm | Find a seat |
| Fix things | Repair cafe - Saturday at 2 pm | Bring one item |

Only the event text changes. Colours, positions and font sizes stay fixed.
The file records the instruction, generator version, seed and variant. Its briefs
are newly authored teaching material, not collected user data.

The first check deliberately trains and inspects output on these same four pairs.
This asks whether the training setup can learn its examples at all. Success would
support a basic engineering check; it would not demonstrate performance on unseen
briefs. No untouched test set has been created. Reserve separate event families
before testing generalisation, as described below.

**Learner task:** suppose the model reproduces all four layouts. Explain what
that establishes and what remains untested. Then move to setting up the local
training tools and inspecting an encoded batch, one step at a time.

## Question and expectation

Can a small sequence model trained from scratch learn to reproduce a handful of
brief/layout pairs? Expect its loss on those examples to decrease. Treat failure
to do so as a reason to inspect the data, target shift, masks and training loop.
Even successful memorisation does not establish useful output on new briefs.

## Proposed setup and bounds

- Local CPU first, a small recurrent sequence model, byte tokens, random initial
  weights and no pretrained model download. This makes the training loop small
  enough to inspect before introducing a transformer or LoRA.
- Four short, self-authored fictional training briefs. Keep the five already
  inspected bundled briefs as development material. Before any generalisation
  experiment, create a separate, immutable test file with different event
  families; all variants of a family belong to the same split. Do not inspect
  test outcomes to choose training settings.
- Fix template variant 0 and seed 0; use the renderer-field target from the
  worked example. Templates are teaching targets, not human endorsements.
- Propose at most 200 updates or two minutes of training, whichever comes first,
  with the same data and settings throughout. Record failure at the limit;
  agree a changed hypothesis before any longer run. Installation time is separate.
- Use a separate training environment. PyTorch is a candidate dependency, subject
  to verifying a compatible package and its licence before installation.
  [PyTorch's licence](https://github.com/pytorch/pytorch/blob/main/LICENSE) includes
  BSD-style terms and third-party notices. No external dataset or model licence
  is needed for random weights and our own fictional examples. The project's
  public source/data licence remains an open decision before inviting reuse.

## Evidence required from the executable exercise

1. Print one decoded input/target batch. Verify next-token shift, inclusion of
   the first layout token and end marker, and exclusion of prompt/padding labels.
2. Record machine, Python/library versions, model configuration, parameter count,
   seed, exact examples/splits and data hash. Set and record the run bounds.
3. Record loss before training and after the final update on the same examples,
   number of updates, elapsed time and stop reason. Check for non-finite values.
4. Generate from the brief alone, without feeding in the target. Preserve raw
   output; separately report JSON validity, correct text and required fields,
   structural checks, and visual observations. Malformed output is a result.
5. Save weights, configuration and token mapping; reload in a fresh process and
   reproduce a saved deterministic output. This is an inference reload check;
   a fully resumable training checkpoint will also need optimiser and random state.
6. The learner interprets the loss and at least one generated output. Distinguish
   agent-run engineering checks from training personally inspected by the learner.

## Local preflight, 10 October 2026

The existing project environment has Python 3.14.3 and its developer check tools.
Neither that environment nor system Python has PyTorch, MLX or NumPy installed.
The filesystem reported about 771 GiB free. `vm_stat` reported roughly 0.87 GiB
of free pages at inspection; this is not total available/reclaimable memory and
does not prove training memory fit. The earlier recorded machine is an Apple M5
with 24 GiB unified memory; sandbox restrictions prevented a fresh `sysctl` check.

Recheck memory pressure and package compatibility immediately before setup, then
prove one forward/backward step and save/reload on the selected device. Accelerator
support remains untested; if considered later, follow the
[PyTorch MPS availability check](https://docs.pytorch.org/docs/2.14/notes/mps.html).
No packages, models or datasets were downloaded during this preflight.
