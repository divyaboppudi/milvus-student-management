from pydantic import BaseModel


class StudentUpdateRequest(BaseModel):
    name: str
    grade: str
    subjects: list[str]

    row_version: int