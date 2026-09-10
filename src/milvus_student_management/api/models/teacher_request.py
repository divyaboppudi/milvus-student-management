from pydantic import BaseModel


class TeacherRequest(BaseModel):
    name: str
    department: str
    subjects: list[str]