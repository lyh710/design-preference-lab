# Learning state — start here

Last updated: 10 October 2026, Sydney time.
This is the authoritative resume point. Update it after each substantive session.

## Outcome and working agreement

Develop hands-on ability to train, adapt, debug and evaluate generative models,
with reproducible research that the learner can explain in an interview. The two
target roles, their requirements, the learner's starting point and why they shape
this project are documented in [role-context.md](role-context.md). Read that brief
before selecting lessons; use [the roadmap](learning-roadmap.md) for the sequence.

The learner has substantial research and LLM-evaluation experience. Personal
generative-model training is the priority gap. Use the existing app to support
experiments; avoid letting app polish or introductory evaluation exercises delay
training. The repo holds lasting decisions, learning progress and next steps so
a fresh chat can resume without the old conversation.
The reusable new-chat prompt lives in [RESUME.md](../RESUME.md), linked from the
README; remembering or retrieving the prompt from a chat is not the learner's task.

Daily sessions are intended to last 15–20 minutes: brief recap, one concept,
one prediction/change/inspection, and a short interpretation. Longer experiments
need separate time agreed with the learner. The assistant prepares supporting
code, tests and explanations; the learner makes research choices and explains
results. A working implementation alone is not evidence of learner mastery.

## Current checkpoint

| Area | Actual status / evidence |
| --- | --- |
| App | Template baseline implemented: brief → two JSON layouts → SVG → saved preference → structural checks. See [README](../README.md). |
| Engineering verification | Initial source commit `cb2c5c9`; 12 tests, lint, type checks, package build and browser walkthrough passed. [GitHub run](https://github.com/lyh710/design-preference-lab/actions/runs/38023702581) succeeded. See [verification](verification.md) for limits. |
| Learner observation | Preferred the left poster because the headline felt “more centered and clear.” Both displayed the same structural metrics. This is one qualitative observation, not a study result. |
| Intro exercise | One comparison discussed. The full three-brief exercise was not completed; it is optional practice, not a prerequisite for starting training. |
| Actual ML training | Not started. No learned generator, LoRA adapter, visual evaluator or reward model exists. No training loss or model-quality improvement has been measured. |
| Guided lessons | Lesson 01 steps 1–2 discussed. The learner identified long-title fit/overlap risk and predicted fixed layout structure would be easier to learn than copying changing event text. Four [training pairs](lessons/examples/01-training-pairs.json) are prepared for step 3. No executable training loop exists yet. |

## Next unfinished lesson: 01 — what does the generator learn?

**Status:** steps 1–2 discussed; step 3 training examples prepared for inspection.
The learner explicitly requested one step at a time, with the purpose explained.

**Purpose:** connect the current brief/layout representation to actual supervised
training, then prepare the first tiny local training experiment.

**Resume at the learner discussion:**

1. Continue at step 3 in [the experiment card](lessons/01-tiny-experiment.md): inspect
   the four training pairs and discuss what memorising them can and cannot show.
   The learner has selected this direction and requested that the exercise begin;
   keep moving one step at a time. Their step 3 interpretation is not yet recorded.
2. Next, introduce the local setup and proposed run bounds (200 updates or two
   minutes), then inspect the actual encoded input/target and loss mask before
   training. Token masking and loss were explained but have not yet been verified
   through the learner's inspection of a real batch. Confirm understanding through
   that inspection. Reserve separate event families before testing generalisation.
3. Recheck current resources and select compatible training tools. Preflight found
   no training libraries in the existing project or system Python environment;
   package compatibility and accelerator support remain unverified. Use a separate
   training environment. Explain dependencies and licensing before downloads.
   No cloud resources or pretrained model downloads are needed for this first run.

**Lesson completion evidence:** the worked example and chosen experiment are
committed, and the learner has explained what the model predicts, what its loss
measures, and why lower loss alone does not establish better design quality.
Record which explanations were actually demonstrated and what remains unclear.
The first training run is a subsequent checkpoint: record the real command,
configuration, loss, generated examples and successful checkpoint reload.

## Environment and boundaries

- Verified on 10 October 2026: Apple M5 Mac, 24 GiB unified memory, Python 3.14.3.
  Recheck current free resources and training-library compatibility before setup.
- Runtime app uses Python's standard library; developer checks use the tools in
  `requirements-dev.txt`. Commands are in the README. A new checkout may need setup.
- Local database and browser state are ignored by git. A fresh clone can run the
  examples but will not contain the learner's raw votes. The qualitative observation
  above is preserved independently. A server running in an old chat is not guaranteed
  to remain available; inspect/start it when needed.
- No paid compute, model download or cloud budget is approved by this checkpoint.
  Obtain separate approval for spending and bound total exposure before cloud work.
- Use fictional, self-authored or appropriately licensed public data. Keep private
  employment information and raw personal notes out of this public repository.

## Daily session / reminder status

**Configured and active:** standalone automation
`design-preference-lab-daily-learning`, daily at **7 pm Australia/Sydney**, starting
**11 October 2026**. Verified on 10 October by creating/updating the task and
reading back its saved configuration. It points to this GitHub repo and is not
attached to the chat that created it. Local execution requires the Mac to be on
and the desktop app running. A successful scheduled run has not yet been observed.

Read [daily-session.md](daily-session.md) for its saved prompt, run instructions,
verification limits and recovery procedure. Unattended runs invite participation
and resume the unfinished lesson; they do not advance learning or modify the repo.

## Open decisions

- Confirm the first actual daily run; configuration is verified, execution is not yet observed.
- Complete the Lesson 01 discussion, agree the detailed tiny-run checks and select
  compatible local tools. The brief-to-layout training direction is selected.
- Choose a public source license before inviting reuse; none has been selected.

For historical decisions and learner observations, read [the session log](session-log.md).
