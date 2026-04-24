import pytest

from app.domain.project import ProjectStatus
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse


def test_project_status_values():
    assert ProjectStatus.ACTIVE == "ACTIVE"
    assert ProjectStatus.ARCHIVED == "ARCHIVED"


def test_project_create_defaults():
    project = ProjectCreate(name="My Project", owner_id="user-001")
    assert project.status == ProjectStatus.ACTIVE
    assert project.description is None


def test_project_create_explicit_values():
    project = ProjectCreate(
        name="Archived Project",
        owner_id="user-002",
        description="Old project",
        status=ProjectStatus.ARCHIVED,
    )
    assert project.status == ProjectStatus.ARCHIVED
    assert project.description == "Old project"


def test_project_create_name_max_length():
    valid = ProjectCreate(name="A" * 255, owner_id="user-001")
    assert len(valid.name) == 255

    with pytest.raises(Exception):
        ProjectCreate(name="A" * 256, owner_id="user-001")


def test_project_update_all_optional():
    update = ProjectUpdate()
    assert update.name is None
    assert update.description is None
    assert update.status is None


def test_project_update_partial():
    update = ProjectUpdate(status=ProjectStatus.ARCHIVED, name="Renamed")
    assert update.status == ProjectStatus.ARCHIVED
    assert update.name == "Renamed"
    assert update.description is None


def test_project_update_name_max_length():
    valid = ProjectUpdate(name="B" * 255)
    assert len(valid.name) == 255

    with pytest.raises(Exception):
        ProjectUpdate(name="B" * 256)


def test_project_response_from_attributes():
    from datetime import datetime, timezone
    from unittest.mock import MagicMock

    now = datetime.now(timezone.utc)
    mock_orm = MagicMock()
    mock_orm.id = "proj-001"
    mock_orm.name = "Test Project"
    mock_orm.description = None
    mock_orm.status = ProjectStatus.ACTIVE
    mock_orm.owner_id = "user-001"
    mock_orm.created_at = now
    mock_orm.updated_at = now

    response = ProjectResponse.model_validate(mock_orm)
    assert response.id == "proj-001"
    assert response.name == "Test Project"
    assert response.status == ProjectStatus.ACTIVE
