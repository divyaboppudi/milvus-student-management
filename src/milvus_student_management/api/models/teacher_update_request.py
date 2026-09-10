from pydantic import BaseModel


class TeacherUpdateRequest(BaseModel):
    name: str
    department: str
    subjects: list[str]

    row_version: int