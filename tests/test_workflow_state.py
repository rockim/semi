import pytest

from app.domain.workflow_state import WorkflowStateCategory
from app.schemas.workflow_state import (
    WorkflowStateCreate,
    WorkflowStateUpdate,
    WorkflowStateResponse,
)


def test_workflow_state_category_values():
    assert WorkflowStateCategory.TODO == "TODO"
    assert WorkflowStateCategory.IN_PROGRESS == "IN_PROGRESS"
    assert WorkflowStateCategory.DONE == "DONE"


def test_workflow_state_create_defaults():
    state = WorkflowStateCreate(name="To Do", project_id="proj-001", display_order=0)
    assert state.category == WorkflowStateCategory.TODO
    assert state.is_default is False
    assert state.description is None
    assert state.color is None


def test_workflow_state_create_explicit_values():
    state = WorkflowStateCreate(
        name="Done",
        project_id="proj-001",
        display_order=2,
        category=WorkflowStateCategory.DONE,
        color="#00FF00",
        is_default=True,
    )
    assert state.category == WorkflowStateCategory.DONE
    assert state.color == "#00FF00"
    assert state.is_default is True


def test_workflow_state_create_name_max_length():
    valid = WorkflowStateCreate(name="A" * 100, project_id="p", display_order=0)
    assert len(valid.name) == 100

    with pytest.raises(Exception):
        WorkflowStateCreate(name="A" * 101, project_id="p", display_order=0)


def test_workflow_state_create_color_max_length():
    valid = WorkflowStateCreate(name="State", project_id="p", display_order=0, color="#FFFFFF")
    assert valid.color == "#FFFFFF"

    with pytest.raises(Exception):
        WorkflowStateCreate(name="State", project_id="p", display_order=0, color="#FFFFFFF0")


def test_workflow_state_update_all_optional():
    update = WorkflowStateUpdate()
    assert update.name is None
    assert update.category is None
    assert update.display_order is None
    assert update.is_default is None


def test_workflow_state_update_partial():
    update = WorkflowStateUpdate(category=WorkflowStateCategory.IN_PROGRESS, is_default=True)
    assert update.category == WorkflowStateCategory.IN_PROGRESS
    assert update.is_default is True
    assert update.name is None


def test_workflow_state_update_name_max_length():
    with pytest.raises(Exception):
        WorkflowStateUpdate(name="B" * 101)


def test_workflow_state_response_from_attributes():
    from datetime import datetime, timezone
    from unittest.mock import MagicMock

    now = datetime.now(timezone.utc)
    mock_orm = MagicMock()
    mock_orm.id = "ws-001"
    mock_orm.name = "In Progress"
    mock_orm.description = None
    mock_orm.color = "#0000FF"
    mock_orm.category = WorkflowStateCategory.IN_PROGRESS
    mock_orm.project_id = "proj-001"
    mock_orm.display_order = 1
    mock_orm.is_default = False
    mock_orm.created_at = now
    mock_orm.updated_at = now

    response = WorkflowStateResponse.model_validate(mock_orm)
    assert response.id == "ws-001"
    assert response.category == WorkflowStateCategory.IN_PROGRESS
    assert response.display_order == 1
