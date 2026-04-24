# SEMI-TASK-005

## Title
Workflow state model

## Requirement
SEMI-REQ-005

## Description
프로젝트별 커스터마이징 가능한 워크플로우 상태 엔티티를 구현한다.
WorkflowState는 Issue의 진행 단계를 나타내며 이름, 색상, 카테고리, 순서를 관리한다.

## Scope
- `app/domain/workflow_state.py` — WorkflowState SQLAlchemy 모델 + WorkflowStateCategory Enum
- `app/schemas/workflow_state.py` — WorkflowStateCreate / WorkflowStateUpdate / WorkflowStateResponse
- `tests/test_workflow_state.py` — 9개 단위 테스트

## Acceptance Criteria
- `pytest tests/test_workflow_state.py` 통과
- `name` max_length=100, `color` max_length=7 강제
- WorkflowState 모델에 name, description, color, category, project_id, display_order, is_default 필드 존재

## Assignee
Claude (Developer)

## Status
Completed

## Branch
feature/SEMI-TASK-005-workflow-state-model

## Traceability
- Requirement: SEMI-REQ-005
- Commit: (this commit)
- QA Report: (pending Codex review — will be updated with report ID after QA pass)
- Release Note: docs/release-notes/v0.2.0.md (planned)
