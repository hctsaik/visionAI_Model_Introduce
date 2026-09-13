# WI-038 requirement change: demand-led PoC

## ADDED Requirements

### Requirement: infer a method from everyday requirements
The assistant SHALL ask one relevant dropdown question at a time. Model selection SHALL NOT be a required input. Every question SHALL offer an unknown answer. Selecting an answer SHALL require explicit Continue before advancing.

#### Scenario: fixed-grid missing part
Given fixed positions and readable images, the result proposes aligned per-location checking. When placement changes to arbitrary, the result changes to locating each object before counting.

#### Scenario: missing evidence
Unknown conditions SHALL remain unresolved. Poor image visibility SHALL prioritize imaging improvements. Millimetre measurement without calibration SHALL prioritize a reference and calibration. Normal-only data SHALL NOT establish defect recall.

### Requirement: explain and export a trial
Results SHALL show method steps, answer-based reasons, missing prerequisites and a small independent-data experiment. Optional course examples SHALL follow the result. Users SHALL be able to export Markdown and JSON and print the trial.

### Requirement: durable safe editing
Changing an upstream answer SHALL invalidate dependent answers and confirmations. Legacy drafts SHALL remain available in a separate historical area and JSON backup, and SHALL NOT determine new recommendations. Reset and example replacement SHALL support undo. Learning progress SHALL remain independent of PoC reset.

## Validation

Six scenarios and metamorphic checks are in tests/test_poc_decision.cjs; browser journeys and persistence/export checks are in tests/test_poc_workbench.py. WI-037/DESIGN.md records design rationale. Actual execution results belong to REPORT.md and verification receipts, not this specification.
