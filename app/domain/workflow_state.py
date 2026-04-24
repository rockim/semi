import enum
from typing import Optional

from sqlalchemy import Boolean, Enum as SAEnum, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.base import BaseModel


class WorkflowStateCategory(str, enum.Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class WorkflowState(BaseModel):
    __tablename__ = "workflow_states"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    color: Mapped[Optional[str]] = mapped_column(String(7), nullable=True)
    category: Mapped[WorkflowStateCategory] = mapped_column(
        SAEnum(WorkflowStateCategory),
        default=WorkflowStateCategory.TODO,
        nullable=False,
    )
    project_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    display_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    is_default: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
