# SEMI-TASK-003

## Title
Issue domain model

## Requirement
SEMI-REQ-003

## Description
FastAPI + SQLAlchemy 2.x 기반 프로젝트 뼈대를 구성하고 Issue 도메인 모델을 구현한다.
Issue는 semi의 핵심 엔티티로, 상태(Status), 우선순위(Priority), 유형(Type)을
enum으로 관리하며 Pydantic v2 스키마로 입출력을 검증한다.

## Scope
- `requirements.txt` / `requirements-dev.txt` 의존성 정의
- `app/` 패키지 구조 생성 (core, domain, schemas)
- `app/core/config.py` — Pydantic Settings 기반 환경설정
- `app/core/database.py` — SQLAlchemy 2.x engine / Base / get_db
- `app/domain/base.py` — id(UUID), created_at, updated_at 공통 베이스
- `app/domain/issue.py` — Issue SQLAlchemy 모델 + Enum 정의
- `app/schemas/issue.py` — IssueCreate / IssueUpdate / IssueResponse Pydantic 스키마
- `alembic.ini` + `alembic/env.py` — 마이그레이션 기반 설정
- `tests/test_issue.py` — Enum 및 Pydantic 스키마 단위 테스트

## Acceptance Criteria
- `pytest tests/` 통과
- Issue 모델에 title, description, status, priority, issue_type, project_id, assignee_id, reporter_id, due_date 필드 존재
- IssueCreate / IssueUpdate / IssueResponse 스키마 동작
- `app/` 디렉터리 구조가 Phase 3 API 구현을 수용할 수 있는 형태

## Assignee
Claude (Developer)

## Status
Completed

## Branch
feature/SEMI-TASK-003-issue-domain-model

## Traceability
- Requirement: SEMI-REQ-003
- Commit: 5073e80
- QA Report: QA-2026-04-24-008 (findings resolved in SEMI-TASK-015)
- Release Note: docs/release-notes/v0.2.0.md (planned)
