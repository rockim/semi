# SEMI-REQ-004

## Title
Project 도메인 모델

## Description
semi 시스템에서 Issue를 묶는 상위 엔티티인 Project를 정의한다.
Project는 이름, 설명, 상태, 소유자를 가지며 Issue의 `project_id`와 연결된다.

## Acceptance Criteria

1. Project 엔티티는 다음 필드를 가진다:
   - `id` (UUID, PK)
   - `name` (str, 필수, max 255)
   - `description` (str, 선택)
   - `status` (enum: ACTIVE / ARCHIVED)
   - `owner_id` (str, 필수)
   - `created_at`, `updated_at` (자동 관리)
2. Pydantic v2 스키마 ProjectCreate / ProjectUpdate / ProjectResponse 존재
3. `ProjectCreate.name` 및 `ProjectResponse.name`은 max_length=255 강제
4. `pytest tests/` 통과

## Linked Task
- SEMI-TASK-004

## Status
Completed
