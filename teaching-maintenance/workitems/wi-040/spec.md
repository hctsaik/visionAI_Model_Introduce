# WI-040 Change requirements

Import MUST validate course-backup structure and supported version before confirmation or mutation. Existing v1/v2 backups without a type marker remain accepted when their full base structure matches. v1 migrates to v2 with an empty draft if absent. New exports include backupType=vision-ai-learning-progress. Invalid files, cancellation and storage failure preserve original progress. Unknown backup versions and malformed known draft structures are rejected.

Homepage MUST expose a primary demand-assistant button to #view=poc at desktop and mobile widths; lesson reading remains accessible.

ConvNeXt, V-JEPA and AnomalyGPT rendered mechanism text MUST match its headings and distinguish original model processing from optional application integration. The change preserves all lesson images and other topics.

Acceptance: tests/test_release_hardening.py, existing PoC tests, compiled data delta restricted to three topics' mechanism_steps, actual desktop/mobile screenshots and public deployment hash/browser smoke. No claim of full 319-image scoring or human learning validation.
