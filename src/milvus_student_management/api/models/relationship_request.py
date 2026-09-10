from pydantic import BaseModel


class RelationshipRequest(BaseModel):
    relationship_type: str
    source_id: str
    target_id: str