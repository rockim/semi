# semi Agent Guide

## Project
semi는 Jira의 핵심 기능을 대체하기 위한 이슈/프로젝트/워크플로우 관리 시스템이다.

## Agent Roles

### Claude - Developer
- 기능 개발 담당
- 요구사항 문서를 먼저 읽고 구현한다.
- 구현 전 관련 task 파일을 확인한다.
- 구현 후 변경 파일, 의도, 영향 범위를 agent log에 남긴다.
- 직접 QA 완료라고 판단하지 않는다.

### Codex - QA
- 코드 리뷰, 테스트 설계, 결함 탐지 담당
- Claude가 구현한 내용을 기준으로 요구사항 충족 여부를 검증한다.
- QA 결과는 docs/agent-logs/codex-qa/ 에 기록한다.
- 결함 발견 시 tasks/ 하위에 후속 task를 생성한다.

## Mandatory Workflow
1. README.md 확인
2. ROADMAP.md 확인
3. TODO.md 확인
4. 관련 requirements 문서 확인
5. 관련 task 파일 확인
6. 작업 수행
7. 로그 작성
8. Git commit 메시지 작성 제안

## Traceability Rule
모든 기능은 아래 항목이 연결되어야 한다.

Requirement ID → Task ID → Commit → QA Report → Release Note

예:
SEMI-REQ-002 → SEMI-TASK-002 → commit hash → QA-2026-04-24-001 → v0.1.0

# Git / GitHub Rules

## Repository
This project is managed in GitHub as the semi development repository.

## Claude Developer Rules
Claude is responsible for implementation.

Before coding:
1. Run `git status`
2. Check current branch
3. Read `TODO.md`
4. Read related task file under `tasks/`

During coding:
1. Modify only files related to the assigned task
2. Do not mix unrelated refactoring
3. Keep commits small and traceable

After coding:
1. Run tests if possible
2. Run `git diff`
3. Update the related task file
4. Write a dev log under `docs/agent-logs/claude/`
5. Create a commit

## Commit Rule
Commit message format:

[SEMI-TASK-001] Short summary

Examples:
[SEMI-TASK-001] Initialize project structure
[SEMI-TASK-002] Add issue domain model
[SEMI-TASK-003] Implement project CRUD API

## Branch Rule
Use one branch per task.

Branch format:

feature/SEMI-TASK-001-project-structure
feature/SEMI-TASK-002-issue-model
fix/SEMI-TASK-005-issue-validation

## Push Rule
After successful commit:

git push origin <branch-name>

## Pull Request Rule
Each task should be reviewed through a GitHub Pull Request.

PR title format:

[SEMI-TASK-001] Initialize project structure

PR must include:
- linked task
- changed files
- test result
- Claude dev log path
- Codex QA report path
