# SEMI-REQ-005

## Title
Workflow state 모델

## Description
프로젝트별로 커스터마이징 가능한 이슈 워크플로우 상태를 정의한다.
WorkflowState는 Issue의 진행 단계를 나타내며 프로젝트마다 고유하게 구성된다.

## Acceptance Criteria

1. WorkflowState 엔티티는 다음 필드를 가진다:
   - `id` (UUID, PK)
   - `name` (str, 필수, max 100)
   - `description` (str, 선택)
   - `color` (str, 선택, max 7 — hex color code)
   - `category` (enum: TODO / IN_PROGRESS / DONE)
   - `project_id` (str, 필수)
   - `display_order` (int, 필수)
   - `is_default` (bool, 기본값 False)
   - `created_at`, `updated_at` (자동 관리)
2. Pydantic v2 스키마 WorkflowStateCreate / WorkflowStateUpdate / WorkflowStateResponse 존재
3. `WorkflowStateCreate.name`은 max_length=100 강제
4. `WorkflowStateCreate.color`는 max_length=7 강제
5. `pytest tests/` 통과

## Linked Task
- SEMI-TASK-005

## Status
Completed
