from milvus_student_management.infrastructure.ai.tools.relationship_tool import (
    RelationshipTool,
)


class RelationshipAgent:

    def __init__(
        self,
        relationship_tool: RelationshipTool,
    ):
        self.relationship_tool = relationship_tool

    def get_relationship_details(
        self,
        relationship_id: str,
    ):

        return (
            self.relationship_tool.get_relationship(
                relationship_id
            )
        )