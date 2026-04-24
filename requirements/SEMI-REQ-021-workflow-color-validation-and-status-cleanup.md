# SEMI-REQ-021

## Title
Workflow color 유효성 검사 강제 및 SEMI-TASK-005 상태 정리

## Description
QA-2026-04-24-016이 두 가지 Major 항목을 발견했다:
1. `WorkflowStateCreate.color`가 hex 형식이 아닌 값을 허용함
2. `TODO.md` Backlog에 SEMI-TASK-005가 중복으로 존재

## Acceptance Criteria

1. `color` 필드는 `#RGB` 또는 `#RRGGBB` 형식만 허용한다 (regex 검증).
2. `nothex`, `FFFFFF` 등 잘못된 값은 ValidationError로 거부된다.
3. 유효/무효 color 형식을 검증하는 테스트가 존재한다.
4. `TODO.md` Backlog에 SEMI-TASK-005가 없다.
5. `tasks/SEMI-TASK-005-*.md` traceability가 QA-2026-04-24-016을 참조한다.

## Linked Task
- SEMI-TASK-021

## Trigger
- QA-2026-04-24-016 (SEMI-TASK-005 FAIL)

## Status
Completed
