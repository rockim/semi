# SEMI-REQ-001

## Title
Project folder structure and documentation baseline

## Description
The semi repository must have a documented, consistent folder structure so that all agents (Claude Developer, Codex QA) and human contributors can navigate the codebase, locate task definitions, requirements, and QA artifacts without ambiguity.

## Acceptance Criteria

1. Repository root contains: `README.md`, `AGENTS.md`, `ROADMAP.md`, `TODO.md`, `.gitignore`
2. `tasks/` directory exists and holds individual task definition files named `SEMI-TASK-NNN-*.md`
3. `requirements/` directory exists and holds requirement files named `SEMI-REQ-NNN-*.md`
4. `docs/agent-logs/claude/` directory exists for Claude developer logs
5. `docs/agent-logs/codex-qa/` directory exists for Codex QA reports
6. No editor backup or unrelated artifacts are tracked by git
7. A git repository is initialized with at least one commit on `main`

## Linked Task
- SEMI-TASK-001

## Status
In Review
