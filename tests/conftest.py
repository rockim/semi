import pytest


@pytest.fixture
def sample_issue_data():
    return {
        "title": "Test Issue",
        "description": "A test description",
        "project_id": "proj-001",
        "reporter_id": "user-001",
    }
