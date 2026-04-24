from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from app.domain.workflow_state import WorkflowStateCategory


class WorkflowStateCreate(BaseModel):
    name: str = Field(max_length=100)
    description: Optional[str] = None
    color: Optional[str] = Field(None, max_length=7, pattern=r'^#[0-9A-Fa-f]{3}([0-9A-Fa-f]{3})?$')
    category: WorkflowStateCategory = WorkflowStateCategory.TODO
    project_id: str
    display_order: int = 0
    is_default: bool = False


class WorkflowStateUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = None
    color: Optional[str] = Field(None, max_length=7, pattern=r'^#[0-9A-Fa-f]{3}([0-9A-Fa-f]{3})?$')
    category: Optional[WorkflowStateCategory] = None
    display_order: Optional[int] = None
    is_default: Optional[bool] = None


class WorkflowStateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str = Field(max_length=100)
    description: Optional[str]
    color: Optional[str] = Field(None, max_length=7, pattern=r'^#[0-9A-Fa-f]{3}([0-9A-Fa-f]{3})?$')
    category: WorkflowStateCategory
    project_id: str
    display_order: int
    is_default: bool
    created_at: datetime
    updated_at: datetime
