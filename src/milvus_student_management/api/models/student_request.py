from pydantic import BaseModel


class StudentRequest(BaseModel):

    name: str
    grade: str
    subjects: list[str]