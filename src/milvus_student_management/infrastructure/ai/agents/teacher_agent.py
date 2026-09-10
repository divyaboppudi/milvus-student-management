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