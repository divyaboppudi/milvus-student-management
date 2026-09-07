from pydantic import BaseModel, Field
from uuid import uuid4

from milvus_student_management.domain.enums.entity_type import EntityType


class Student(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    entity_type: EntityType = EntityType.STUDENT

    name: str
    grade: str

    subjects: list[str] = []