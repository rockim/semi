# SEMI-REQ-017

## Title
SEMI-TASK-016 상태 문서 일관성 확보

## Description
QA-2026-04-24-010이 SEMI-TASK-016 task 파일(Completed)과
ROADMAP/TODO(In Progress)의 상태 불일치를 발견했다.
이 반복 패턴을 종료하기 위해 016, 017 모두를 단일 커밋에서 완전히 닫는다.

## Acceptance Criteria

1. `ROADMAP.md`에서 SEMI-TASK-016, SEMI-TASK-017 모두 `Completed`.
2. `TODO.md` Active 섹션에 016, 017이 없고 Completed 섹션에 존재한다.
3. `tasks/SEMI-TASK-016-*.md` traceability가 QA-2026-04-24-010을 참조한다.
4. `tasks/SEMI-TASK-017-*.md` traceability가 SEMI-REQ-017을 참조한다.

## Linked Task
- SEMI-TASK-017

## Trigger
- QA-2026-04-24-010 (SEMI-TASK-016 FAIL)

## Status
Completed
