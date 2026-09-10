from pydantic import BaseModel


class ParentRequest(BaseModel):
    name: str
    phone_number: str