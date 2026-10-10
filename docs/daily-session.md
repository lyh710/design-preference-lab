# Daily learning session

## Verified schedule configuration

- Name: Design Preference Lab — daily learning.
- Automation ID: `design-preference-lab-daily-learning`.
- Status verified on 10 October 2026: **ACTIVE**.
- Cadence: daily at **19:00 Australia/Sydney**, starting **11 October 2026**.
  The saved recurrence explicitly includes this timezone and start date.
- Execution: standalone local scheduled task, with no parent chat or project
  attachment required. Each run starts from the GitHub repository, not a previous
  conversation or the original working folder.
- Model at setup: `gpt-6.1-sol`, medium reasoning. Recheck availability if changing
  the automation later.
- The Mac must be on and the desktop app running for local execution. The repo
  records the setup but is not itself a scheduler. Confirmed configuration is not
  evidence of a successful scheduled run; the first run has not occurred yet.

The creation tool reported success, and the saved automation file was read back
to verify its active status, standalone target, repository prompt and recurrence.
An earlier conversation claimed a separate ChatGPT reminder existed; that hosted
reminder was never independently verified. If it later appears, reconcile it with
this named task rather than running two daily learning programmes.

## Saved scheduler prompt

> Open https://github.com/lyh710/design-preference-lab and read the latest RESUME.md
> and docs/daily-session.md. Follow the repository instructions to resume the next
> unfinished daily learning session. Use actual repository contents as the source
> of truth, without relying on any prior chat. If the files cannot be read, notify
> the learner of that limitation instead of inventing progress.

## Instructions for each scheduled run

1. Read the latest committed `RESUME.md`, `AGENTS.md`, `docs/role-context.md`,
   `docs/learning-state.md`, and the latest entry in `docs/session-log.md`. Follow
   links needed for the next lesson. Retrieve actual files, not search snippets.
2. Notify the learner that the daily 15–20 minute session is ready. Briefly explain
   where they left off, which role-related capability the next step develops, and
   present one small question or hands-on step.
3. Wait for the learner to respond before advancing. If the last lesson is
   unfinished, continue it. A missed day does not create a completed lesson or
   justify skipping to the next one.
4. Keep the unattended run read-only. Do not mark completion, write session logs,
   fabricate research results, launch training, download models, start paid
   services or mutate the repository merely because the schedule fired.
5. Once the learner participates, use the repo's teaching and persistence rules:
   record actual observations and decisions, distinguish learning from engineering
   progress, and commit/push substantive public-safe updates with verification.
   Preserve unrelated changes and keep private data and credentials out of git.

If tools, repository access or required local files are unavailable, report the
specific limitation. Never silently replace the recorded lesson with a generic
topic or assume that an unavailable local dataset exists in a fresh checkout.

## Recreating or checking the schedule

Look up the automation ID above in the app before creating another schedule.
Use the saved prompt, daily 7 pm Sydney time, and a standalone destination. The
schedule must survive removal of the originating chat and must not target it.
Read back the saved settings after a change; record verified changes here and
link them from `docs/learning-state.md`. Confirm a real run separately in the
app's Scheduled view.

Reference: [official scheduled-task documentation](https://learn.chatgpt.com/docs/automations?surface=app).
