from app.domain.issue import IssuePriority, IssueStatus, IssueType
from app.schemas.issue import IssueCreate, IssueUpdate, IssueResponse


def test_issue_status_values():
    assert IssueStatus.TODO == "TODO"
    assert IssueStatus.IN_PROGRESS == "IN_PROGRESS"
    assert IssueStatus.IN_REVIEW == "IN_REVIEW"
    assert IssueStatus.DONE == "DONE"


def test_issue_priority_values():
    assert IssuePriority.LOW == "LOW"
    assert IssuePriority.MEDIUM == "MEDIUM"
    assert IssuePriority.HIGH == "HIGH"
    assert IssuePriority.CRITICAL == "CRITICAL"


def test_issue_type_values():
    assert IssueType.BUG == "BUG"
    assert IssueType.FEATURE == "FEATURE"
    assert IssueType.TASK == "TASK"
    assert IssueType.STORY == "STORY"


def test_issue_create_defaults(sample_issue_data):
    issue = IssueCreate(**sample_issue_data)
    assert issue.status == IssueStatus.TODO
    assert issue.priority == IssuePriority.MEDIUM
    assert issue.issue_type == IssueType.TASK
    assert issue.description == "A test description"
    assert issue.assignee_id is None
    assert issue.due_date is None


def test_issue_create_explicit_values():
    issue = IssueCreate(
        title="Bug Report",
        project_id="proj-002",
        reporter_id="user-002",
        status=IssueStatus.IN_PROGRESS,
        priority=IssuePriority.CRITICAL,
        issue_type=IssueType.BUG,
    )
    assert issue.status == IssueStatus.IN_PROGRESS
    assert issue.priority == IssuePriority.CRITICAL
    assert issue.issue_type == IssueType.BUG


def test_issue_update_all_optional():
    update = IssueUpdate()
    assert update.title is None
    assert update.status is None
    assert update.priority is None
    assert update.issue_type is None


def test_issue_update_partial():
    update = IssueUpdate(status=IssueStatus.DONE, priority=IssuePriority.HIGH)
    assert update.status == IssueStatus.DONE
    assert update.priority == IssuePriority.HIGH
    assert update.title is None


def test_issue_response_from_attributes():
    from datetime import datetime, timezone
    from unittest.mock import MagicMock

    now = datetime.now(timezone.utc)
    mock_orm = MagicMock()
    mock_orm.id = "issue-001"
    mock_orm.title = "Test"
    mock_orm.description = None
    mock_orm.status = IssueStatus.TODO
    mock_orm.priority = IssuePriority.MEDIUM
    mock_orm.issue_type = IssueType.TASK
    mock_orm.project_id = "proj-001"
    mock_orm.assignee_id = None
    mock_orm.reporter_id = "user-001"
    mock_orm.due_date = None
    mock_orm.created_at = now
    mock_orm.updated_at = now

    response = IssueResponse.model_validate(mock_orm)
    assert response.id == "issue-001"
    assert response.title == "Test"
    assert response.status == IssueStatus.TODO
