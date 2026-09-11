from pydantic import BaseModel


class Base64FileRequest(
    BaseModel
):
    file_name: str
    content: str
