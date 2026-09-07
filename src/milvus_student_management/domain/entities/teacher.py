from uuid import uuid4

from pydantic import BaseModel, Field

from milvus_student_management.domain.enums.entity_type import EntityType


class Teacher(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    entity_type: EntityType = EntityType.TEACHER

    name: str
    department: str

    subjects: list[str] = []