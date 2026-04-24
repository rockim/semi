import enum
from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, Enum as SAEnum, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.base import BaseModel


class IssueStatus(str, enum.Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    IN_REVIEW = "IN_REVIEW"
    DONE = "DONE"


class IssuePriority(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class IssueType(str, enum.Enum):
    BUG = "BUG"
    FEATURE = "FEATURE"
    TASK = "TASK"
    STORY = "STORY"


class Issue(BaseModel):
    __tablename__ = "issues"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[IssueStatus] = mapped_column(
        SAEnum(IssueStatus), default=IssueStatus.TODO, nullable=False
    )
    priority: Mapped[IssuePriority] = mapped_column(
        SAEnum(IssuePriority), default=IssuePriority.MEDIUM, nullable=False
    )
    issue_type: Mapped[IssueType] = mapped_column(
        SAEnum(IssueType), default=IssueType.TASK, nullable=False
    )
    project_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    assignee_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    reporter_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    due_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
