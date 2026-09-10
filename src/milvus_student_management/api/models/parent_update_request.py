from pydantic import BaseModel


class ParentUpdateRequest(BaseModel):
    name: str
    phone_number: str

    row_version: int