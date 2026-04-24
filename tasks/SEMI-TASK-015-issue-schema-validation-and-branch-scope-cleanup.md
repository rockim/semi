# SEMI-TASK-015

## Title
Enforce issue schema validation and clean branch scope

## Trigger
- Raised from QA report `QA-2026-04-24-008`

## Related Task
- `SEMI-TASK-003`

## Problem
- `IssueCreate.title` does not enforce the required `max 255` validation rule.
- The `SEMI-TASK-003` branch includes unrelated file `docs/agent-logs/codex-qa/QA-2026-04-24-007.md`.

## Required Actions
1. Update the issue Pydantic schema so `title` enforces the documented max length.
2. Add or update tests to cover the title length validation rule.
3. Remove unrelated Phase 1 QA artifacts from the `SEMI-TASK-003` branch scope, or explicitly document and justify the exception if history cannot be changed.
4. Update `tasks/SEMI-TASK-003-issue-domain-model.md` traceability with the latest QA result once resolved.

## Acceptance Criteria
- `IssueCreate` rejects titles longer than 255 characters.
- Automated tests cover the validation rule.
- The `SEMI-TASK-003` branch contains only task-related files, or any exception is explicitly documented and approved.
- `SEMI-TASK-003` traceability references the resolving QA report.

## Assignee
Claude (Developer)

## Status
Completed

## Branch
feature/SEMI-TASK-015-issue-schema-validation-and-branch-scope-cleanup

## Scope Exception — QA-2026-04-24-007.md
`QA-2026-04-24-007.md` was an untracked file at the time SEMI-TASK-003 work began.
It had not been committed to any branch (including main). To prevent loss of the artifact
it was included in the SEMI-TASK-003 commit. The file's content is legitimate Phase 1 QA
history and does not affect Phase 2 implementation correctness. Removing it from committed
git history would require destructive rewrite; the exception is documented here instead.

## Traceability
- Requirement: SEMI-REQ-003
- Trigger QA: QA-2026-04-24-008
- Commit: 3a453cf
- Release Note: docs/release-notes/v0.2.0.md (planned)
