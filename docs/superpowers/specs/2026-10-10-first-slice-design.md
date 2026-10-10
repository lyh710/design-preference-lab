# Design Preference Lab: first slice

## Intent and scope
Build a personal research portfolio by learning to train design generators and evaluate whether improvements matter to people. The user explicitly requested design and implementation of an executable thin slice in this session. Keep this first design short and execute locally; revisit choices together after trying it. No cloud spend or model downloads in this milestone.

## Choice
Use an event-poster comparison app. An evaluator-only project misses hands-on generator training; a diffusion-first project adds hardware and data complexity before the measurement loop exists. A structured layout provides editable outputs, deterministic rendering and a compact training target.

## First user journey
Enter a title, event details and call to action; generate two template layouts with a seed; inspect both; select left, right, tie or neither. Save the vote, its displayed order and optional reason, then reveal structural metrics. Reload and export the recorded session. Generation is explicitly template-based, not a trained model. Single-user local operation only.

## Components
Python 3.11+ standard library, no runtime dependencies. `core.py` owns validated briefs, fixed-canvas layouts, escaped SVG rendering and geometric/contrast checks. `store.py` owns SQLite persistence of immutable comparisons and one preference per comparison. `server.py` serves a small browser app and JSON API on 127.0.0.1. `__main__.py` starts the app or writes reproducible example artifacts. Later model adapters replace the generator without changing layout or preference contracts.

## Data and measurement
Schema and generator versions, seed, brief, canonical design IDs, displayed order, SVGs and metrics accompany each comparison. Content IDs use a stable JSON hash. Left/right order is randomized independently of generation seed and persisted. SQLite stores UTC vote timestamps and anonymous optional rationale. No real names. All user data and experiment runs are git-ignored. Five fictional briefs are committed.

Metrics report out-of-canvas boxes, intersecting text boxes, estimated text fit and text/background contrast. They do not measure aesthetics, true font glyph bounds, or image overlap. Report individual checks rather than a misleading composite beauty score. The first app supports Latin-script examples; other scripts are accepted but font fallback/fit requires manual inspection. Browser font rendering may differ by machine; structured layouts and SVG source are reproducible, pixels are not yet pinned.

## Error handling and boundaries
Validate strings and seed ranges; reject oversized/malformed JSON, duplicate votes and unknown comparison IDs. Use SQLite transactions, parameterized queries, escaped text, a request size limit and same-origin browser mutations. Never execute supplied markup. Bind only to loopback and document this is a development app, not a hosted multi-user service.

## Definition of done
Tests demonstrate deterministic layouts, distinct variants, valid escaped SVG, metric failure detection, input rejection, persistence after reopening, immutable votes, blinded API responses, export and real HTTP round trips. Start app and inspect the full browser flow. Run all tests, available lint/type tools and a five-brief repeatability check. Prepare git-ready files and CI; publish only if authentication works. Record actual verification and limitations.

## Next boundary
Actual model training is milestone two, not part of this template baseline. Before selecting a model, confirm available memory and license. Collected single-user preferences are workflow data, not evidence of population preference or evaluator validity. No trained quality model, diffusion, distributed training or performance result is claimed now.
