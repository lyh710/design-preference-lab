# Resuming this project

This repository is the durable record for the project and its learning programme.
Chat history is optional context, not the source of progress or decisions.

## Start every new working session

1. Read `docs/learning-state.md` first. It names the next unfinished lesson,
   current constraints, unresolved decisions and evidence of completed work.
2. Read the latest entry in `docs/session-log.md` and the material linked for that
   next action. Consult `docs/learning-roadmap.md` when planning a new milestone.
3. Inspect `git status` and recent commits before editing. Preserve unrelated
   changes. Establish the checkout's revision and remote status before assuming
   it matches GitHub; never reset local work to obtain a newer checkpoint.
4. Briefly tell the learner where they left off and the next concrete step.
   Resume there; ask only for information absent from the repository or now stale.

## Teach through the project

Use plain language, one concept and one small experiment per session. Explain why
the step matters for model training or evaluation. Have the learner predict,
inspect or interpret a result. Distinguish code built by an agent, experiments
actually run, and understanding demonstrated by the learner. Advancement requires
the lesson's recorded completion evidence, not elapsed days or generated code.

## End every substantive session

- Update `docs/learning-state.md` with the precise next action and remaining work.
- Append a short dated entry to `docs/session-log.md`: decisions, actual work,
  evidence, learner observations, open questions and any changed constraints.
- Commit public-safe learning materials and state together with related changes;
  push verified session updates to the agreed project remote within the user's
  authorization. Report the commit and whether it reached GitHub. Identify any work
  still only local or uncommitted so another checkout does not assume it is saved.
- Preserve confidential notes, raw preference records, credentials and large
  artifacts outside tracked files. Commit safe summaries and reproduction steps;
  mark unavailable evidence honestly instead of inventing results.

Keep current progress only in `docs/learning-state.md`; historical sessions live
in the log. The roadmap describes direction, and the README describes operation.
Scheduling claims require an actual task record or run evidence. A schedule never
means the learner completed a lesson. Paid compute needs separate approval.
