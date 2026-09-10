from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field

from milvus_student_management.domain.enums.entity_type import (
    EntityType,
)


class Parent(BaseModel):
    id: str = Field(
        default_factory=lambda: str(uuid4())
    )

    entity_type: EntityType = (
        EntityType.PARENT
    )

    name: str
    phone_number: str

    row_version: int = 1

    created_at: datetime = Field(
        default_factory=datetime.utcnow
    )

    updated_at: datetime = Field(
        default_factory=datetime.utcnow
    )

    created_by: str = "system"

    updated_by: str = "system"

    is_deleted: bool = False