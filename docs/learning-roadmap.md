# Learning roadmap: design preference laboratory

This file describes the intended curriculum, not completion status. To start or
resume a session, read [learning-state.md](learning-state.md) first.
## Purpose and boundary
Build practical evidence that you can train and evaluate generative systems, using a
small, reproducible project: **event-poster brief → JSON layout → SVG → rule checks
→ blinded human pairwise preferences**. The initial application is deliberately a
Python-standard-library template baseline. It makes no machine-learning claim.

Use only self-authored, synthetic, or clearly licensed public material. Do not put
employer data, customer work, personal contact details, or proprietary career
examples into the repository, prompts, datasets, screenshots, or portfolio.

The goal is decision-quality artefacts, not a promised score, model size, or timeline.
Keep every experiment local until a separately approved cloud budget and run plan exist.
## Working method
For each milestone, write a one-page experiment card before running it:

- Question and falsifiable expectation.
- Fixed inputs, model/data versions and licences, seed, machine/accelerator details.
- Primary metric, error slices, stop condition, and what result would change next.
- A compact result note: aggregate result, counterexamples, costs measured locally,
  limitations, and the next decision.
Keep an immutable `heldout_briefs.jsonl` from the first split onward. Never select
prompts, hyperparameters, templates, or model checkpoints on it. Store examples and
human labels with anonymous rater IDs; randomise left/right display and hide system
identity while a comparison is being made.

## Milestone 0 — deterministic, inspectable baseline
**Build.** Define a versioned JSON schema for an event brief and layout. Implement a
stdlib-only renderer that chooses among explicit layout templates, emits SVG, and
runs deterministic checks: required fields, page bounds, overlap, contrast and
estimated text fit. Save the JSON, SVG, rule report, template version,
and seed beside every result.

**Learn by doing.** Create 30–60 synthetic briefs covering sparse/dense copy,
long titles, small venues, different aspect ratios, and intentionally impossible
requests. Write a failure taxonomy before looking at outcomes.

**Portfolio evidence.** A runnable baseline, schema, ten representative output
pairs, an error-table showing rule failures, and a short design note explaining what
the rule checks can and cannot judge.

**Gate.** You can reproduce an SVG and its rule report from a saved record, and can
show at least one rule-compliant poster that a person still prefers less.

## Milestone 1 — human preference is the reference signal
**Build.** Make a small local comparison interface or static packet. For each brief,
show two shuffled candidates and ask a focused question such as “which better serves
the event brief?” plus an optional reason chosen from a fixed taxonomy. Include a
tie/unsure option. Pre-register the comparison protocol and exclusion rules.

**Learn by doing.** Compare template variants and deliberately trade one design
quality against another. Audit left/right bias, agreement, ties, and disagreement by
brief slice. Read individual disagreements before collapsing them into a win rate.

**Portfolio evidence.** The rubric, rater instructions, blinded-results table,
agreement/disagreement analysis, and a decision memo naming a metric that was
misleading or incomplete.

**Gate.** You can explain a material human–rule-check disagreement with examples,
rather than treating either signal as ground truth.

## Milestone 2 — train locally, then adapt with LoRA
This milestone is non-negotiably hands-on: first train a genuinely tiny model locally,
then fine-tune an existing permissively licensed small model with LoRA. Do not replace
either part with API prompting or a notebook walkthrough.

### 2A. Tiny training run
**Build.** Train a tiny causal sequence model on synthetic brief-to-layout tokens (or
a constrained text representation of the JSON). Write the loss loop yourself enough
to inspect inputs, target shift, padding, and masks. Hold out briefs, not random rows,
to avoid near-duplicate leakage.

**Experiments.** Overfit a handful of examples as a sanity check; then compare a
baseline versus one changed factor (data size, sequence length, or constraint token).
Inspect sampled failures and whether valid JSON/rule compliance moves separately from
human preference.

**Portfolio evidence.** Dataset generator and licence note; loss curves; a table of
parameter count, trainable count, seed, and held-out results; sample decodes; and a
short explanation of the token-level cross-entropy objective and every masked token.

### 2B. LoRA adaptation
**Build.** Select a small model only after checking its licence, redistribution terms,
and local memory fit. Freeze the base model, add LoRA adapters, print the all versus
trainable parameter counts, and save the adapter configuration with the base-model
revision. LoRA freezes the original weights and trains low-rank update matrices;
adapter rank and target modules determine the added capacity.

Use completion-only supervision: prompt/brief, schema instructions, and padding must
have label `-100`; only intended layout completion tokens contribute to loss. Confirm
this with one inspected batch. Save a full resumable checkpoint (adapter, optimiser,
scheduler, RNG state, tokenizer, config, data manifest, and step) and a separate
inference export. Reload in a new process and reproduce a saved output.

**Experiments.** Hold data and training budget fixed while varying one factor such as
LoRA rank or target modules. Compare base, adapter, and template baseline on untouched
briefs and the human-pairwise protocol. Report malformed JSON, rule failures, and
preference separately. Manually inspect regressions instead of averaging them away.

**Portfolio evidence.** A minimal training command; data card; model/licence record;
trainable-parameter printout; mask visualisation; checkpoint/reload proof; and a
held-out comparison report with enough artefacts for another person to audit it.

**Gate.** A fresh local process reloads the saved adaptation, and the untouched-brief
report distinguishes training loss from useful poster quality.

## Milestone 3 — efficient adaptation and evaluation models
**QLoRA.** Only after standard LoRA works, use 4-bit quantisation plus LoRA. Record
quantisation settings, compute dtype, platform support, and any quality or stability
change. QLoRA reduces weight memory; it does not make results comparable to an
industrial multi-GPU training run.

**Learned evaluator.** Build a simple preference predictor first from frozen features
or a small licensed vision-language model (VLM), trained on paired human labels. Keep
brief, candidates, rater splits, and evaluation briefs disjoint where possible.
Measure calibration, pairwise agreement, error slices, and confidence intervals or
resampling uncertainty. Treat it as a diagnostic judge, not an automatic reward.

**Reward-hacking test.** Optimise candidates against the evaluator, then send those
candidates to blinded humans and to a held-out judge/rubric. Report every case where
the evaluator improves while human preference falls, and judge-disagreement rate by
slice. This is the central evidence against using a convenient proxy as truth.

**Portfolio evidence.** An evaluator card, split diagram, calibration/error report,
adversarial/reward-hacking examples, and a written “do not use for” boundary.

## Milestone 4 — multimodal generation and scale
**Diffusion/design generation.** Add generated imagery only when its licence and
training-data conditions are documented. Evaluate image suitability separately from
layout, legibility, and brief fulfilment; a visually attractive image can still make a
bad poster.

**Multi-GPU.** Learn distributed data parallelism, mixed precision, sharding, failure
recovery, and experiment tracking through a documented small reproduction. Any cloud
multi-GPU work requires a separately approved provider, region, instance count,
maximum spend, shutdown rule, and reproducibility plan before resources are started.
Do not treat a Mac run as equivalent to industrial multi-GPU training: it is useful
for local development and controlled learning, but has different accelerators,
memory, kernels, throughput, and distributed systems behaviour.

**Portfolio evidence.** A reproducibility bundle: pinned environment, dataset/model
manifests and licences, seeds, command lines, configurations, checkpoint lineage,
hardware notes, and a rerun report. Include negative results and known failure modes.

## Hardware and model selection: prerequisites, not assumptions
Choose hardware or a base model only after recording all of the following:

1. Actual free RAM and unified-memory behaviour under a baseline run; available disk
   for model, checkpoints, and data; operating-system and accelerator support.
2. The candidate model’s exact revision, licence, acceptable-use terms, tokenizer,
   context length, parameter count, dtype/quantisation support, and local memory
   estimate including optimiser and activations.
3. The dataset and image asset licences, redistribution permissions, and provenance.
4. A small dry run proving load, inference, one backward pass, checkpoint write, and
   clean reload on the intended machine.

If any item fails, reduce scope or change the experiment; do not buy hardware or start
paid compute to force it through.

## How this maps to the supplied roles
| Role | Evidence this roadmap deliberately builds |
| --- | --- |
| [Canva Principal Research Scientist – Evaluations](https://www.linkedin.com/jobs/view/4459354951/) | Human-preference protocol, rubric and rater reliability; correlation and disagreement between judges and users; evaluator/reward-model limits; multimodal quality and launch-style regression gates. |
| [Canva Senior Research Scientist – Design Generation](https://www.linkedin.com/jobs/view/4460307145/) | End-to-end scoped research, real training and LoRA, data/objective choices, held-out evaluation, design-generation failure analysis, then a bounded path to diffusion and multi-GPU practice. |

The learner already brings evaluation leadership; the gap addressed here is personal,
auditable training practice and its interaction with preference measurement.

## Technical sources consulted
- [Hugging Face PEFT: LoRA](https://huggingface.co/docs/peft/main/conceptual_guides/lora) — frozen base weights, trainable low-rank updates, and adapter configuration.
- [Hugging Face Transformers: fine-tuning](https://huggingface.co/docs/transformers/training) and [TRL SFT Trainer](https://huggingface.co/docs/trl/sft_trainer) — causal-LM collation and completion-only loss masking using `-100` labels.
- [PyTorch: Save and Load the Model](https://docs.pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html) — state dictionaries and safe weight loading.
- [Hugging Face Transformers: bitsandbytes quantisation](https://huggingface.co/docs/transformers/main/quantization) — 4-bit quantisation and QLoRA context.

## Session planning

The next lesson, current environment evidence and unresolved decisions are maintained
in [learning-state.md](learning-state.md). Advance by demonstrated learning and
experiment evidence, rather than a fixed number of calendar days.
