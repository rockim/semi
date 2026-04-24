# SEMI-TASK-004

## Title
Project domain model

## Requirement
SEMI-REQ-004

## Description
Project 도메인 모델 및 Pydantic v2 스키마를 구현한다.
Project는 Issue의 상위 그룹 엔티티로, 이름/설명/상태/소유자를 관리한다.

## Scope
- `app/domain/project.py` — Project SQLAlchemy 모델 + ProjectStatus Enum
- `app/schemas/project.py` — ProjectCreate / ProjectUpdate / ProjectResponse
- `tests/test_project.py` — 8개 단위 테스트

## Acceptance Criteria
- `pytest tests/test_project.py` 통과
- `ProjectCreate.name` 및 `ProjectUpdate.name`에 max_length=255 강제
- Project 모델에 name, description, status, owner_id 필드 존재

## Assignee
Claude (Developer)

## Status
Completed

## Branch
feature/SEMI-TASK-004-project-domain-model

## Traceability
- Requirement: SEMI-REQ-004
- Commit: 0d91a79
- QA Report: QA-2026-04-24-012
- Release Note: docs/release-notes/v0.2.0.md (planned)
