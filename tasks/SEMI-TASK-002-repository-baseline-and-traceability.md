# SEMI-TASK-002

## Title
Establish repository baseline and documentation traceability for initial project setup

## Trigger
- Raised from QA report `QA-2026-04-24-001`
- Related failed review target: `SEMI-TASK-001`

## Problem
- The workspace is not a Git repository.
- Mandatory workflow documents are missing.
- The baseline folder structure for requirements, tasks, and logs is missing.
- A backup artifact `AGENTS.md~` exists in the repository root.
- The traceability chain required by `AGENTS.md` cannot be formed.

## Required Actions
1. Initialize or restore the Git repository used for the project.
2. Add mandatory files:
   - `ROADMAP.md`
   - `TODO.md`
3. Add baseline directories and seed documents:
   - `requirements/`
   - `tasks/`
   - `docs/`
4. Create the formal task definition document for `SEMI-TASK-001`.
5. Define the requirement linked to `SEMI-TASK-001` with a `SEMI-REQ-*` identifier.
6. Remove non-project backup artifacts from tracked scope and prevent recurrence if needed.
7. Resolve the QA log path inconsistency between:
   - `docs/agent-logs/codex-qa/`
   - `docs/04-agent-logs/codex-qa/`

## Acceptance Criteria
- `git status` runs successfully in the project root.
- `ROADMAP.md`, `TODO.md`, a related requirement document, and a related task document all exist.
- The repository contains the agreed documentation directories.
- No editor backup or unrelated artifact remains in task scope.
- `SEMI-TASK-001` can be traced to a requirement and a commit.

## Requirement
SEMI-REQ-002

## Assignee
Claude (Developer)

## Status
In Progress

## Branch
feature/SEMI-TASK-002-repository-baseline

## Traceability
- Requirement: SEMI-REQ-002
- Commit: (pending)
- QA Report: (pending)
- Release Note: v0.1.0 (planned)

## Suggested Commit Message
[SEMI-TASK-002] Establish repository baseline and traceability
