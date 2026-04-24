# SEMI-REQ-015

## Title
Issue schema title 길이 제약 강제 및 브랜치 스코프 예외 문서화

## Description
SEMI-REQ-003의 Acceptance Criteria에 명시된 `title max 255` 제약이
API 레이어(Pydantic 스키마)에서 강제되지 않았다. 또한 Phase 1 QA 아티팩트가
SEMI-TASK-003 브랜치에 의도치 않게 포함된 사유를 문서화해야 한다.

## Acceptance Criteria

1. `IssueCreate.title`은 255자 초과 입력을 Pydantic ValidationError로 거부한다.
2. `IssueResponse.title`도 동일한 max_length 제약을 보유한다.
3. 255자 허용, 256자 거부를 검증하는 자동화 테스트가 존재한다.
4. `QA-2026-04-24-007.md`가 SEMI-TASK-003 브랜치에 포함된 사유가 task 문서에 명시된다.

## Linked Task
- SEMI-TASK-015

## Trigger
- QA-2026-04-24-008 (SEMI-TASK-003 FAIL)

## Status
Completed
