from milvus_student_management.infrastructure.ai.tools.student_tool import (
    StudentTool,
)

from milvus_student_management.infrastructure.ai.tools.relationship_tool import (
    RelationshipTool,
)

from milvus_student_management.infrastructure.ai.tools.parent_tool import (
    ParentTool,
)


class StudentAgent:

    def __init__(
        self,
        student_tool: StudentTool,
        relationship_tool: RelationshipTool,
        parent_tool: ParentTool,
    ):
        self.student_tool = (
            student_tool
        )

        self.relationship_tool = (
            relationship_tool
        )

        self.parent_tool = (
            parent_tool
        )

    def get_student_details(
        self,
        student_id: str,
    ):
        return (
            self.student_tool.get_student(
                student_id
            )
        )

    def get_all_students(
        self,
    ):
        return (
            self.student_tool.get_all_students()
        )

    def search_students(
        self,
        query: str,
    ):
        return (
            self.student_tool.search_students(
                query
            )
        )

    def get_student_context(
        self,
        student_id: str,
    ):

        student = (
            self.student_tool.get_student(
                student_id
            )
        )

        relationships = (
            self.relationship_tool.get_student_relationships(
                student_id
            )
        )

        return {
            "student": student,
            "relationships": relationships,
        }