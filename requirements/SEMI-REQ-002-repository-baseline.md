# SEMI-REQ-002

## Title
Repository baseline and documentation traceability

## Description
All blockers and major findings from `QA-2026-04-24-001` must be resolved so that
`SEMI-TASK-001` becomes fully traceable and the repository is in a clean, reviewable
state. This includes fixing the QA log path inconsistency in `AGENTS.md`, confirming
that no backup artifacts are tracked, and ensuring every required traceability chain
element exists.

## Acceptance Criteria

1. `AGENTS.md` uses a single, consistent path for Codex QA logs: `docs/agent-logs/codex-qa/`
2. `AGENTS.md~` is not tracked by git (covered by `.gitignore`)
3. `SEMI-TASK-001` traceability chain is complete:
   - Requirement: `SEMI-REQ-001`
   - Task: `tasks/SEMI-TASK-001.md`
   - Commit: recorded in task file
   - QA Report: `docs/agent-logs/codex-qa/QA-2026-04-24-001.md`
4. `SEMI-TASK-002` itself has a requirement (`SEMI-REQ-002`), task file, dev log, and commit
5. `ROADMAP.md` and `TODO.md` reflect current task statuses

## Linked Task
- SEMI-TASK-002

## Status
In Progress
