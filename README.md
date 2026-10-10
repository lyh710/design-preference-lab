# Design Preference Lab

A small research app for asking: **does better measured design quality mean people prefer the result?**

**Why this project exists:** preparation for Canva's Principal Research Scientist –
Evaluations and Senior Research Scientist – Design Generation roles, through
hands-on research. [Read the role context and learning priorities](docs/role-context.md).

Enter an event-poster brief → generate two structured layouts → render SVG → choose a preference → inspect structural checks. This is the first executable slice of a longer generator-training and learned-evaluation project.

**Current status:** local template baseline. There is no trained generator, learned evaluator, human study result, or cloud deployment yet. This is an independent personal project, not affiliated with Canva.

## Resume learning here

Read [the role context](docs/role-context.md), then **[learning-state.md](docs/learning-state.md)**. The latter records what has
actually been completed, the next unfinished lesson, working agreements and open
questions. [The session log](docs/session-log.md) preserves past decisions and
observations. [The roadmap](docs/learning-roadmap.md) explains the longer-term path.

**[Copy the saved new-chat prompt from RESUME.md](RESUME.md).** You do not need
to remember the prompt or retrieve the previous conversation.

The new chat needs access to the repository contents; a name alone is insufficient.
Use the latest pushed commit when starting elsewhere. Local-only or uncommitted
work cannot be recovered from a fresh GitHub checkout. Private raw records remain
local; public-safe summaries and reproduction instructions are committed.

## Run locally

Requires Python 3.11 or newer. No runtime dependencies, API keys, model downloads or paid services.

```sh
python3 -m design_lab
```

Open http://127.0.0.1:8765. Run from the repository folder. Stop with Ctrl+C. Use `python3 -m design_lab serve --port 8766` for another port. The server binds only to this computer; it is not designed for public hosting.

1. Enter a short title, event details and a call to action.
2. Generate two candidates. The brief and seed determine the layouts; displayed left/right order is shuffled independently.
3. Judge communication, readability, hierarchy and appeal. Choose left, right, tie, or neither; optionally explain why.
4. The vote is saved, then metrics appear. Reload preserves the most recent comparison in this browser. Use **Export local records** for JSON records.

An experiment records the actual brief used, even if you subsequently edit the form. Each comparison permits one immutable vote. A new generation creates a new record. Browser storage remembers only the latest record ID; SQLite is the source of truth. Data lives in `data/preferences.sqlite`, ignored by git. Export includes briefs and free-text reasons: review it before sharing.

## Reproduce the baseline

```sh
python3 -m design_lab demo --output runs/demo
python3 -m unittest discover -s tests -v
```

The five fictional briefs in `design_lab/examples/briefs.json` produce ten SVGs and a manifest containing layouts, seeds, versions, IDs and metrics. Rerunning with the same code and Python version reproduces these files byte for byte. Display order, record IDs and timestamps in the interactive app deliberately differ. SVG source is stable; exact pixels depend on browser/font rendering.

## What is measured

| Check | Meaning | Limitation |
| --- | --- | --- |
| Boxes outside canvas | Count of text boxes crossing the canvas boundary | Does not inspect individual glyphs |
| Overlapping text boxes | Count of intersecting text-box pairs | Decorative shapes are excluded |
| Estimated text overflows | Approximate wrapped text height exceeds its box | Uses estimated character width, not measured glyph bounds |
| Minimum contrast ratio | Lowest text/background luminance contrast | Assumes a solid background; not an accessibility certification |

There is deliberately no combined “beauty score.” Automated checks and template identity are hidden before voting. Source code and exported geometry still make template identity inferable: this is a workflow demonstration, not secure experimental blinding. The two templates vary hierarchy with shared colours; this does not establish generalisation beyond that narrow comparison. A single person's choices cannot establish population preference. Latin-script briefs are the tested starting point; inspect other scripts and font fallback manually.

## Research and learning

[Learning roadmap](docs/learning-roadmap.md) stages tiny training, real LoRA adaptation, quantised adaptation, multimodal preference models, reward-hacking experiments, diffusion and separately budgeted multi-GPU work. Training comes next; UI expansion should not postpone it.

The [first experiment](docs/first-experiment.md) is optional introductory practice:
compare three briefs and look for a pair where identical structural metrics hide
a meaningful preference. These labels are practice records, not a statistically
powered dataset. Follow the next lesson in [learning-state.md](docs/learning-state.md)
when resuming; completing this optional exercise is not a gate to model training.

Each later experiment should state its hypothesis first, separate development and untouched test briefs, record model/data revisions, report failure slices and uncertainty, and include a short research memo. Keep private or employer material out of the repository. See the [design](docs/superpowers/specs/2026-10-10-first-slice-design.md) and [implementation plan](docs/superpowers/plans/2026-10-10-first-slice.md).

## Development

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/ruff check .
.venv/bin/ruff format --check .
.venv/bin/mypy
.venv/bin/python -m build --no-isolation
```

`core.py` owns generation/rendering/checks; `store.py` owns SQLite records; `server.py` owns the HTTP boundary; `static/` owns presentation; `__main__.py` owns app/demo commands. Use tests first for behaviour changes. CI runs tests, lint, type checking and build; local verification evidence is in [verification.md](docs/verification.md).

## Publishing

Keep SQLite, local runs, private labels, credentials and model weights out of commits. A public source license has not been chosen yet; choose one before inviting reuse or distributing third-party datasets/models.
