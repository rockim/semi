# SEMI-TASK-021

## Title
Enforce workflow color validation and clean task status

## Trigger
- Raised from QA report `QA-2026-04-24-016`

## Related Task
- `SEMI-TASK-005`

## Problem
- `WorkflowStateCreate.color` accepts non-hex strings even though the requirement defines it as a hex color code.
- `TODO.md` lists `SEMI-TASK-005` in both Backlog and Completed.

## Required Actions
1. Update workflow state schema validation so `color` only accepts valid hex color values consistent with the requirement.
2. Add or update tests to cover valid and invalid color formats.
3. Remove `SEMI-TASK-005` from the Backlog section of `TODO.md` so status is unambiguous.
4. Update `tasks/SEMI-TASK-005-workflow-state-model.md` traceability with the resolving QA report once complete.

## Acceptance Criteria
- Invalid color values such as `nothex` are rejected by schema validation.
- Tests cover both valid and invalid color inputs.
- `TODO.md` no longer shows `SEMI-TASK-005` in Backlog.
- `SEMI-TASK-005` traceability references the resolving QA report.

## Assignee
Claude (Developer)

## Status
Completed

## Branch
feature/SEMI-TASK-005-workflow-state-model

## Traceability
- Requirement: SEMI-REQ-021
- Trigger QA: QA-2026-04-24-016
- Commit: d22ec75
- QA Report: QA-2026-04-24-017 (findings resolved in SEMI-TASK-022)
- Release Note: docs/release-notes/v0.2.0.md (planned)
