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
| Guided lessons | Lesson 01 steps 1–3 discussed: the learner identified layout-fit risk, predicted copying difficulty, and correctly identified unseen-data performance as untested by memorisation. Four training pairs are saved. Step 4 local tools are installed and checked; see [setup](lessons/01-local-setup.md). No sequence-model training loop exists yet. |

## Next unfinished lesson: 01 — what does the generator learn?

**Status:** steps 1–3 discussed; step 4 local environment prepared and checked.
The learner explicitly requested one step at a time, with the purpose explained.

**Purpose:** connect the current brief/layout representation to actual supervised
training, then prepare the first tiny local training experiment.

**Resume at the learner discussion:**

1. Continue with step 5: inspect an actual encoded brief/layout batch. Show the
   prompt, first layout token, end marker and padding; verify the next-token shift
   and which labels contribute to loss. The learner has already identified that
   success on four training examples leaves performance on unseen data untested.
2. Use the separate environment at `runs/lesson01-env`: Python 3.14.3, PyTorch
   2.14.1 and NumPy 2.5.3 on macOS arm64. Exact package versions and setup commands
   are saved in [the setup guide](lessons/01-local-setup.md). CPU scalar forward,
   backward and fresh-process save/reload passed. A sequence model and its memory
   requirements have not yet been tested; accelerator support is untested.
3. Introduce the proposed first-run bound of 200 updates or two minutes before
   running the actual training loop. Preserve raw generated outputs and compare
   the same examples before/after; inspect failures and reload saved model weights.
   Keep the learner involved one step at a time. No cloud resources or pretrained
   model downloads are needed. Reserve separate families before generalisation tests.

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
  the sequence-model configuration. The local CPU tools are installed; the
  brief-to-layout training direction is selected.
- Choose a public source license before inviting reuse; none has been selected.

For historical decisions and learner observations, read [the session log](session-log.md).
