from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from app.domain.project import ProjectStatus


class ProjectCreate(BaseModel):
    name: str = Field(max_length=255)
    description: Optional[str] = None
    owner_id: str
    status: ProjectStatus = ProjectStatus.ACTIVE


class ProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    status: Optional[ProjectStatus] = None


class ProjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str = Field(max_length=255)
    description: Optional[str]
    status: ProjectStatus
    owner_id: str
    created_at: datetime
    updated_at: datetime
