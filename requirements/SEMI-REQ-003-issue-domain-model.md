# SEMI-REQ-003

## Title
Issue 도메인 모델 및 프로젝트 뼈대

## Description
semi 시스템의 핵심 엔티티인 Issue를 정의한다. Issue는 프로젝트 내에서
생성되며 상태, 우선순위, 유형으로 분류된다. 이 요구사항은 Phase 2 도메인
모델의 첫 번째 구현이며, FastAPI 기반 프로젝트 뼈대 설정도 포함한다.

## Acceptance Criteria

1. Issue 엔티티는 다음 필드를 가진다:
   - `id` (UUID, PK)
   - `title` (str, 필수, max 255)
   - `description` (str, 선택)
   - `status` (enum: TODO / IN_PROGRESS / IN_REVIEW / DONE)
   - `priority` (enum: LOW / MEDIUM / HIGH / CRITICAL)
   - `issue_type` (enum: BUG / FEATURE / TASK / STORY)
   - `project_id` (str, 필수)
   - `assignee_id` (str, 선택)
   - `reporter_id` (str, 필수)
   - `due_date` (datetime, 선택)
   - `created_at`, `updated_at` (자동 관리)
2. Pydantic v2 스키마 IssueCreate / IssueUpdate / IssueResponse 존재
3. `pytest tests/` 통과
4. 프로젝트 뼈대 (`app/`, `requirements.txt`, `alembic/`) 존재

## Linked Task
- SEMI-TASK-003

## Status
Completed
