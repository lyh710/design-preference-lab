# Learning session log

Append dated, concise, public-safe entries. Current progress and the next action
belong in [learning-state.md](learning-state.md); this log preserves how decisions
were reached. Record observations as observations, not proven general findings.

## 2026-10-10 — foundation, orientation and durable handover

**Built and checked:** a local template poster-comparison app, reproducible demo,
SQLite preferences, tests and learning roadmap. Source checkpoint `cb2c5c9`.
Twelve tests, lint, type checks, build and browser walkthrough passed; initial
[GitHub checks](https://github.com/lyh710/design-preference-lab/actions/runs/38023702581)
succeeded. No model training took place.

**Learner observation:** chose the left poster and said “headline more centered
and clear.” Both candidates displayed zero detected out-of-bounds boxes, text-box
overlaps and estimated text overflows, with minimum contrast 9.06:1. The vote was
already saved when inspected. The reason was supplied in conversation and is
preserved here; it was not retroactively inserted into the immutable vote record.
The browser automation smoke-test label was kept in a separate ignored database.

**Interpretation:** headline placement/clarity is a candidate explanation for the
preference. A single comparison cannot isolate causation or establish a general
preference. No controlled headline-position experiment has been run.

**Learner feedback and decision:** the connection between poster choices, the repo,
the two roles and daily sessions was unclear. Agreed to use the app as a common
research setup and prioritise hands-on training next. Daily sessions should teach
one concept through one small experiment; substantial training runs may need
separately agreed time. The roadmap is direction, not a completed lesson sequence.

**Durability agreement:** persist necessary decisions, materials, actual progress
and next actions as repo commits. A new chat pointed at the repo must resume from
those files without depending on old conversation history. Added root `AGENTS.md`
and the authoritative learning-state file; the README points to them.

**Unresolved:** the intended daily 7 pm Sydney reminder was not verified. No new
schedule or model-training environment was created. Lesson 01 remains planned.

**Handover checks:** 19 local Markdown links and the resume entry points resolved.
A fresh agent with no chat history correctly recovered completed work, the exact
next lesson and completion evidence, the learner's observation, and the unverified
schedule/cost boundaries using only repo files. It correctly flagged that the
handover would not reach a fresh clone until the documentation was committed and
pushed. This entry is included in that handover commit; use git history and remote
status to establish which checkpoint is available in a new checkout.

## 2026-10-10 — save the restart prompt itself

The learner requested that the restart prompt also live in the repo, rather than
relying on memory or chat history. Saved the prompt in root `RESUME.md` and linked
it from the README and learning state. Lesson 01 remains the next unfinished
lesson; this documentation change does not represent learning progress.

## 2026-10-10 — preserve the roles as the starting brief

The learner clarified that the two applications are the starting context for the
entire programme. The repo had only a short role mapping near the end of the
roadmap. Added `docs/role-context.md` with job titles/IDs/source links, dated
requirement summaries, learner-provided background and priorities, the reason for
the combined project, and the evidence each stage should produce. Distinguished
advertised requirements from our selected learning techniques and future plans.
Linked this brief near the top of README and made it required reading in AGENTS.md.
The next lesson and actual training status are unchanged.
