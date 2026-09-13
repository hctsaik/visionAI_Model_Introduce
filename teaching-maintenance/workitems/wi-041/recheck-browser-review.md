# WI-041 fresh browser and visual review

Date: 2026-09-13. Scope: review only. Product unchanged; user approval pending. No new confirmed UI freeze blocker from this review. Content corrections belong to the independent content review and root adjudication.

## Baseline and automated coverage

- HTTP `http://127.0.0.1:8000/docs/index.html` initially matched local docs SHA-256 `43c3557afba4300ad67425bdaba432e0a3582a14e227af0144711db1c0e75e28`.
- `recheck-coverage-1440.json` and `recheck-coverage-390.json`: 58 lessons at each viewport; 116 lesson visits total. All 4 engineering slide sections per lesson = 464 rendered slide instances. Each lesson answer disclosure clicked = 116. Expanded deep-dive chapters: 40 per viewport, 80 visits. 12 common/family routes per viewport = 24 additional route visits. No recorded route failure, JS exception or document horizontal overflow after harness correction.
- The first fresh detailed run completed 46 desktop lessons with full concept and four-slide zoom clicks, bookmark/complete toggles and navigation checks. Remaining lessons use breadth rendering and family-first interaction checks. Mobile interactive patterns are sampled once for each of 7 families; availability/decode is covered on all 58 lessons. Do not interpret this as every possible hidden variant clicked.
- `recheck-file-image-decode.json`: all 116 lesson visits reopened against the identical docs bundle using Edge `file://` with local file access. All 1,228 main HTML image-node instances decoded, zero broken and zero document overflow. This is artifact/browser-rendering verification, not public transport verification. Root owns public transport/hash checks.

## False positives preserved and settled

- `recheck-browser-coverage.json` keeps 5 original interaction failures (ResNet, SegFormer, PatchCore, AnomalyDINO, EfficientAD). The harness attempted a concept button in an inactive `reading-view-panel[hidden]` without selecting its view; it was not a broken user-facing button. Fresh breadth reruns cover all 5; alternate hidden reading-view variants were not exhaustively clicked.
- Port 8000 intermittently returned/left broken images during parallel heavy reads. Accordingly, `ok` rows mean execution reached the end, NOT that their image-decode fields passed. Those image failures remain in raw evidence and cannot support an all-images-loaded claim. Independent 1,228-node file decode passes. PatchCore was reproduced with its intact first figure using stable port 8014 (`recheck-stable-patchcore-1440.png`); the blank 8000 capture is not a product defect. Exact server root cause was not proven by this agent.
- Earlier extra-interaction attempts used nonexistent sidebar selectors. Final corrected harness targets the observed `data-action="go"` buttons. These are harness corrections, not product changes.

## Actual visual inspection

Separately from automation, directly opened screenshots for the first teaching figure and/or its original-image zoom for all 7 families: ChArUco, ResNet, dense YOLO, PatchCore, Frame Difference, DINOv2 and DefectFill. Desktop full figures plus mobile viewport sections were visually read; PatchCore stable HTTP and full mobile file screenshot checked after initial loading contamination. Their inputs, transformations and output responsibility remain legible in this sample. Mobile vertically arranged figures have readable labels and the explanation follows the picture. No sample requires a site-wide visual redesign before freeze.

Evidence prefixes: `recheck-finalfigure-{1440,390}-<topic>.png`, `recheck-visual-390-<topic>.png`, `recheck-zoom-1440-<topic>.png`. Also directly viewed mobile home, library, foundations, production and glossary route screenshots; primary content and controls remain within viewport. Some element screenshots include a sticky header across the top because Playwright scrolls the tall figure under it; this is a screenshot framing artifact, not evidence that the underlying title is irretrievably clipped. The final HTTP probe records viewport title reachability.

## Limits and optional next work

No numerical quality score is assigned, and this is not a 319-image pixel-by-pixel proofread. Review covers all routes automatically, with manual visual sampling across every family; it does not establish learner understanding, Safari/iOS behavior, real-device touch behavior, every hidden engineering reading view, or exhaustive keyboard/screen-reader accessibility. Native-size zoom requires two-dimensional panning; this is supported behavior with an original-image link, though a fit-to-width/fit-entire-image toggle could reduce reading effort in a later version. It is optional UX work, not a freeze blocker found here.

Additional search, mobile drawer, theme persistence, PatchCore title reachability and lightbox edge results are recorded in `recheck-extra-interactions.json`; see final checkpoint below.

## Final agent checkpoint

Completed: all 116 lessons / 464 slides / 24 common routes; separate all 1,228-image file decode passes. Stable HTTP desktop extra interactions passed: search returned exactly one PatchCore result and opened the lesson; theme persisted after reload; native-size lightbox starts within its left edge and can reach right/bottom edges (numeric bounds in JSON). Mobile stable HTTP viewport screenshot `recheck-title-reachable-390.png` was directly viewed: first figure title is fully reachable below the fixed header, with the PatchCore three-part vertical story legible. This resolves the element-screenshot overlay suspicion.

The final mobile HTTP extra probe was stopped after it reached this screenshot, while awaiting an unbounded image decode promise; no mobile all-actions pass is claimed from its incomplete JSON. Root is performing an independent bounded public mobile smoke to settle the remaining drawer/theme/zoom behavior. This is the only pending review handoff, not a demonstrated product defect. No tests or product edits are pending from this agent. User approval remains pending.

## Root handoff completed

The bounded independent public390px probe completed: search opens PatchCore, drawer closes on navigation, theme persists after reload, figure title sits below the header, zoom reaches all four edges, Escape closes, and no pageerror. See `recheck-public-mobile-ui.json`, `recheck-public-mobile-title.png` and `recheck-public-mobile-zoom-end.png`; root visually inspected both. First root attempt mistakenly awaited all below-fold lazy figures; the successful probe scopes its bounded image wait to the displayed target figure. No product changes were needed. No review handoff remains pending.
