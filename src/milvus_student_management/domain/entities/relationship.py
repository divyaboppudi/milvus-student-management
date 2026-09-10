from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field

from milvus_student_management.domain.enums.relationship_type import (
    RelationshipType,
)


class Relationship(BaseModel):

    id: str = Field(
        default_factory=lambda: str(uuid4())
    )

    relationship_type: RelationshipType

    source_id: str
    target_id: str

    created_at: datetime = Field(
        default_factory=datetime.utcnow
    )

    created_by: str = "system"