# Learning state — start here

Last updated: 10 October 2026, Sydney time.
This is the authoritative resume point. Update it after each substantive session.

## Outcome and working agreement

Develop hands-on ability to train, adapt, debug and evaluate generative models,
with reproducible research that the learner can explain in an interview. The two
target roles are Canva Design Generation and Evaluations; links and competency
mapping are in [the roadmap](learning-roadmap.md).

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
| Guided lessons | Broad roadmap exists. The first guided training lesson and executable training exercise still need to be prepared. |

## Next unfinished lesson: 01 — what does the generator learn?

**Status:** planned, not delivered or completed.

**Purpose:** connect the current brief/layout representation to actual supervised
training, then prepare the first tiny local training experiment.

**At the next session:**

1. Orient the learner in two sentences using this checkpoint. Read
   `design_lab/core.py` and `design_lab/examples/briefs.json` with them as needed.
   Use one example to show the input brief and the layout the model will predict.
2. Prepare `docs/lessons/01-training-example.md` as a short guide: one concrete
   input/target, a plain explanation of next-token prediction and training loss,
   which tokens should contribute to that loss, and two understanding questions.
   This file is a planned deliverable; it does not exist at this checkpoint.
3. Ask the learner to identify the input, target and a likely failure. Agree a
   tiny experiment and its completion checks before constructing the training
   exercise. Keep separate brief families for development and untouched testing.
4. Check installed training tools and current available memory/disk; select a
   small local setup. Plan a tiny model trained from scratch before LoRA. Explain
   dependencies and model/data licensing before downloads. No cloud resources.

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

Intended cadence: **7 pm Australia/Sydney, daily**, originally discussed to start
11 October 2026. Use this timezone across daylight-saving changes.

**Unverified:** the earlier conversation said a reminder was scheduled, but no
matching local Codex automation or verifiable hosted task ID was found during
the 10 October check. No replacement reminder was created. This repo records the
intended schedule; it does not itself run a scheduler. Before creating a reminder,
verify existing tasks to avoid duplicates and confirm its destination with the user.

Any future reminder should point to this repository and resume this file's next
unfinished lesson. It should invite participation, not autonomously mark progress,
run paid experiments or advance to another lesson when the learner is absent.

## Open decisions

- Verify or establish the actual daily reminder and record its task ID/status.
- Select the tiny training experiment and compatible local tools during Lesson 01.
- Choose a public source license before inviting reuse; none has been selected.

For historical decisions and learner observations, read [the session log](session-log.md).
