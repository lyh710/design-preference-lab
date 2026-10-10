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

## 2026-10-10 — standalone daily schedule

Before deleting the original chat, the learner requested verification of a daily
schedule that resumes directly from the repo. No matching local schedule existed.
Created standalone automation `design-preference-lab-daily-learning` and set its
first session to 11 October 2026 at 19:00 Australia/Sydney, recurring daily.
The app reported ACTIVE. It uses a projectless standalone target and a GitHub
repository prompt, with no dependency on the originating chat or working folder.

Saved the session procedure and scheduler prompt in `docs/daily-session.md`, then
updated the automation to read those files. The learner was informed that this
local schedule requires the Mac and desktop app to be running. Configuration is
verified; no scheduled firing or learner completion is claimed. The old hosted
ChatGPT reminder remains unverified, as recorded in the schedule document.
Lesson 01 remains unfinished. The unattended task must invite participation and
must not advance progress or launch training on its own.

Remote retrieval check: raw web reads returned a cache miss; read-only GitHub API
requests successfully retrieved the committed daily-session and learning-state
files using existing authentication with interactive network permission. Added
that fallback to the scheduler prompt and repo instructions. Unattended network
access remains subject to the scheduled run's permissions and has not been proven.

## 2026-10-10 — resume inspection and Lesson 01 preparation

**Repository inspection:** reused the clean existing checkout at `e1e574c` and
verified it matched GitHub. The only local/remote branch was `main`; there were
no stashes, other worktrees, issues or pull requests. The latest five GitHub runs
passed. The referenced “Resume GitHub Project” chat contained a handoff request,
with no additional research decisions. An independent read-only review found no
demonstrable defect in the completed template baseline and identified the missing
Lesson 01 guide as the clear next action.

**Learner decision:** selected “Yes—start with this tiny training exercise” for
a local model learning fictional brief-to-layout pairs from the current templates.
No answer to the follow-up interpretation question has yet been recorded. The
selected direction is preserved; detailed run checks remain proposed.

**Prepared:** `docs/lessons/01-training-example.md` contains a real input/target,
reproduction command, next-token loss explanation, prompt/padding mask and target
shift example, and two understanding questions. The companion experiment card
proposes a small local memorisation run with explicit limits, output inspection
and fresh-process weight reload. No training loop, model, dataset split or measured
training result was created. Updated the README and authoritative resume state.

**Verification:** all 12 existing tests passed with loopback access; lint,
formatting, type checks and source/wheel build passed. The initial restricted test
run had two HTTP setup errors because the sandbox denied socket binding; the same
tests passed after enabling loopback access, without code changes. The lesson's
embedded target exactly matched the template's renderer fields, rendered the same
SVG, and was reproduced by its documented command. All 32 local links checked in
the README, learning state and lesson files resolved. No new browser walkthrough
was needed for these documentation-only changes.

**Environment:** checked project/system Python, installed training libraries,
disk space and memory-page statistics. Findings and limits are in the experiment
card. The developer environment was created with `uv` and lacks `pip`, but already
contains all check tools; no installation was required. Training package
compatibility and accelerator availability remain unverified. No paid resource,
dependency download or training run was started. Learner mastery is not claimed.

## 2026-10-10 — guided steps 1–3 and four teaching pairs

The learner requested simple explanations and one step at a time, then explicitly
asked to start the first training exercise. Step 1 showed a brief and title-box
settings. The learner explained that a longer title could fail to fit, be cut off
or overlap other text. Step 2 introduced next-token training, loss and scoring only
the layout. The learner predicted that repeated structure and colours would be
easier because they stay constant, while event text requires copying from the
brief. This is a prediction to test, not an observed training result. No claim of
demonstrated mask implementation or complete loss understanding is made.

Prepared four self-authored fictional brief/layout pairs for step 3, using seed 0
and variant 0 from the existing generator. Saved the instruction and provenance
with the examples; all four are explicitly training data for a memorisation check.
The learner has yet to interpret what success on these examples would establish.
No untouched test set, training loop, dependency installation or training run was
created. The next practical step after discussion is local setup and inspection of
the encoded batch. The agent prepared the data; the learner did not generate it.

Checked that all four layouts reproduce their template SVGs and have zero detected
out-of-bounds boxes, text-box overlaps and estimated text overflows. These checks
do not establish visual quality. Source code and application behaviour are unchanged.
All 12 existing tests, lint, formatting, type checks and source/wheel build passed;
saved-pair validation and local lesson links also passed.

## 2026-10-10 — unseen-data distinction and local tools

The learner answered that perfect reproduction of the four training pairs leaves
untested “whether it can handle unseen data.” This correctly identifies the
generalisation limit of the memorisation check. Proceeded to step 4 setup without
advancing to model training.

Installed PyTorch 2.14.1 and NumPy 2.5.3 plus their dependencies into the separate,
ignored `runs/lesson01-env`, using the existing Python 3.14.3. Checked official
package compatibility/licensing before installation and saved all resolved package
versions in `requirements-training-macos.txt`. Setup, purpose and reproduction
commands are documented in `docs/lessons/01-local-setup.md`. No pretrained weights,
external dataset, cloud service or paid resource was used.

Ran the guide's two check commands: CPU scalar forward calculation and derivative
both produced the expected 36; the scalar weight stayed 2, and a fresh process
reloaded the saved value. These are framework checks performed by the agent, not
learner-run model training or a model checkpoint test. Confirmed the original app
environment still has no PyTorch. Current next action is inspection of an actual
encoded batch, followed by construction of the bounded training loop.

All 12 app tests, lint, formatting, type checks and source/wheel build passed.
Local setup/lesson links resolve. The documented setup checks ran successfully.

## 2026-10-10 — standing code walkthrough rule and step 5

The learner requested that every learning step show the code, explain it, and
connect it to both the learning topic and the skills needed for their target
roles. Added a standing rule in `AGENTS.md` and references in the resume prompt,
daily-session instructions and learning state. This is a project-wide teaching
preference, not a one-off request. The previous setup guide now also explains its
role connections.

Implemented `design_lab/training_data.py` with byte encoding, explicit next-token
alignment, completion/end-only labels and ignored padding. Its CLI prepares all
four stored examples with no ML dependency or weight update. Added the step 5
code walkthrough, real output, explanations and separate role connections. The
learner has not yet interpreted the shift/mask boundary, so this step remains open.

Five new tests first failed on the missing module, then passed. They cover the
first completion label and end marker, prompt/padding exclusion, Unicode byte
boundaries, refusing truncation, and the real four-example CLI. Full suite: 17
tests passed with loopback access; lint, formatting, type checks (six source
files) and source/wheel build passed. The actual training-environment command
produced four rows of 611 positions. The first has 169 prompt bytes, 426 layout
bytes, 427 scored labels and 16 padding tokens. No model training occurred.

The generated batch is reproducible from committed source and pairs; its local
JSON file stays in ignored `runs/lesson01-batch.json`. The next action is the
learner's code interpretation, then the small model and bounded training loop.

Independent review identified an older illustrative padding row inconsistent with
the chosen shifted representation, and a gap in regression checks for the stored
targets. Aligned the table and strengthened the CLI test to compare stored and
emitted layouts with the fixed template generator and decode the full input. All
17 tests passed again; documented counts matched the actual CLI output and all
56 local Markdown links checked resolved.
