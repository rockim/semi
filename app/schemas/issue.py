from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.domain.issue import IssuePriority, IssueStatus, IssueType


class IssueCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: IssueStatus = IssueStatus.TODO
    priority: IssuePriority = IssuePriority.MEDIUM
    issue_type: IssueType = IssueType.TASK
    project_id: str
    assignee_id: Optional[str] = None
    reporter_id: str
    due_date: Optional[datetime] = None


class IssueUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[IssueStatus] = None
    priority: Optional[IssuePriority] = None
    issue_type: Optional[IssueType] = None
    assignee_id: Optional[str] = None
    due_date: Optional[datetime] = None


class IssueResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    title: str
    description: Optional[str]
    status: IssueStatus
    priority: IssuePriority
    issue_type: IssueType
    project_id: str
    assignee_id: Optional[str]
    reporter_id: str
    due_date: Optional[datetime]
    created_at: datetime
    updated_at: datetime
