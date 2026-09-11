from milvus_student_management.infrastructure.ai.tools.teacher_tool import (
    TeacherTool,
)


class TeacherAgent:

    def __init__(
        self,
        teacher_tool: TeacherTool,
    ):
        self.teacher_tool = teacher_tool

    def get_teacher_details(
        self,
        teacher_id: str,
    ):
        return (
            self.teacher_tool.get_teacher(
                teacher_id
            )
        )

    def get_all_teachers(
        self,
    ):
        return (
            self.teacher_tool.get_all_teachers()
        )

    def search_teachers(
        self,
        query: str,
    ):
        return (
            self.teacher_tool.search_teachers(
                query
            )
        )