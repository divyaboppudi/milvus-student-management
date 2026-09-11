from milvus_student_management.infrastructure.ai.tools.parent_tool import (
    ParentTool,
)


class ParentAgent:

    def __init__(
        self,
        parent_tool: ParentTool,
    ):
        self.parent_tool = parent_tool

    def get_parent_details(
        self,
        parent_id: str,
    ):
        return (
            self.parent_tool.get_parent(
                parent_id
            )
        )

    def get_all_parents(
        self,
    ):
        return (
            self.parent_tool.get_all_parents()
        )

    def search_parents(
        self,
        query: str,
    ):
        return (
            self.parent_tool.search_parents(
                query
            )
        )