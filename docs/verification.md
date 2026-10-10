# First-slice verification

Date: 10 October 2026. Local Python: 3.14.3.

This records engineering checks, not research findings. No model has been trained,
no human study has been run, and the browser automation label is not human data.

## Executed checks

- Test-first stages: core tests initially failed on missing implementation; storage
  and HTTP tests initially failed on missing modules; CLI test failed because no
  command entrypoint existed. Each was implemented and rerun successfully.
- `python -m unittest discover -s tests -v`: 11 tests passed at the initial review
  checkpoint, including actual HTTP requests and persistence across store reopen.
- `ruff check .`: passed. `ruff format --check .`: passed.
- `mypy`: passed for all five application Python files.
- `python -m compileall -q design_lab`: passed.
- `python -m build --no-isolation`: source archive and wheel built successfully.
- Installed the wheel into a separate environment and ran the demo from outside
  the checkout. Five comparison records and ten SVGs were produced; packaged
  browser assets were present.
- CLI regression test generated two separate runs and compared every file byte
  for byte, including the manifest. They matched.
- Browser walkthrough: generate, view both posters, enter a clearly marked test
  reason, save a tie, reveal metrics, reload and observe the preserved vote.
  No captured browser warnings or errors. Narrow and desktop layouts inspected.
- Preview: [app-preview.jpg](app-preview.jpg). Browser smoke data uses a separate
  ignored SQLite database, not the default research database.

## Independent review

A fresh reviewer found no release-blocking issues. One minor finding concerned
unpaired Unicode surrogates in an optional reason. A new regression test reproduced
the failure; explicit validation now rejects it before database work. The final
suite contains 12 tests. Static-route checks also cover HTML, JavaScript and CSS.

## Environment and limitations

The initial sandbox prevented socket binding and made GitHub authentication appear
invalid. With approved loopback/network access, HTTP tests and authentication worked.
No pre-existing code or test baseline existed in the empty workspace.

The GitHub workflow targets Python 3.11 and 3.14 on Linux. Local checks only establish
Python 3.14.3 behaviour on this Mac; remote workflow results must be checked separately.
Browser checking was a manual automated walkthrough, not a persisted browser test suite.
Text geometry is approximate, and exact pixels depend on fonts and browser rendering.

## Reproduction

Follow the commands in the README. Keep experiment input, versions and output
artifacts together. Preserve failures and negative results in later research notes.
