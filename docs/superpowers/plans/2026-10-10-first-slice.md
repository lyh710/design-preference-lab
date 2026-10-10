# First Slice Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans. The parent owns implementation; independent documentation and final review have separate scopes.

**Goal:** Working local brief → comparison → saved preference → revealed metrics/export.
**Architecture:** Pure Python core, SQLite store, loopback HTTP app with static HTML/CSS/JS.
**Tech Stack:** Python 3.11+ standard library and browser SVG.
**Spec:** ../specs/2026-10-10-first-slice-design.md

## Global constraints
No paid calls, model downloads, private data, external assets or runtime dependencies. Template baseline must be visibly labeled. Metrics must remain hidden before a vote. Local runtime records must be excluded from git.

## Review focus
Untrusted brief markup must display as text. Long/empty inputs must fail clearly. Seeds must reproduce source artifacts. Votes must survive restart without permitting duplicates. HTTP errors must leave previous records intact.

## Task 1: Pure design pipeline
Files: `design_lab/core.py`, `tests/test_core.py`, `design_lab/examples/briefs.json`.
Interfaces: `validate_brief(data)`, `generate_pair(brief, seed)`, `render_svg(design)`, `evaluate(design)`, `comparison(brief, seed)`.
- [x] Write tests for deterministic/distinct variants, invalid inputs, escaping and deliberately broken layout checks.
- [x] Run tests; confirm missing implementation failure, implement, then pass tests.

## Task 2: Persistence and HTTP contract
Files: `design_lab/store.py`, `design_lab/server.py`, `tests/test_store.py`, `tests/test_server.py`.
Interfaces: `Store(path).create(brief, seed)`, `.get(id)`, `.vote(id, choice, reason)`, `.export()`; `make_server(port, db_path)`.
- [x] Write tests for restart persistence, duplicate/invalid votes, hidden metrics, JSON export and real HTTP validation.
- [x] Run tests red, implement store and routes, run tests green.

## Task 3: Browser and reproducible demo
Files: `design_lab/static/*`, `design_lab/__main__.py`, `tests/test_cli.py`, README, pyproject, CI.
- [x] Test `python -m design_lab demo --output DIR` produces ten SVGs, manifest and repeatable source output; implement CLI.
- [x] Build responsive comparison UI with loading, errors, vote feedback, session reload and export.
- [x] Verify in browser, run all tests and static checks, independently review; fix material findings with regression tests.
- [x] Record actual results; initialize local git and commit public-safe sources. GitHub creation depends on valid existing authentication.
