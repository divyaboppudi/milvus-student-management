from milvus_student_management.application.services.teacher_service import (
    TeacherService,
)


class TeacherTool:

    def __init__(
        self,
        teacher_service: TeacherService,
    ):
        self.teacher_service = (
            teacher_service
        )

    def get_teacher(
        self,
        teacher_id: str,
    ):

        return (
            self.teacher_service.get_teacher(
                teacher_id
            )
        )

    def search_teachers(
        self,
        query: str,
    ):

        return (
            self.teacher_service.search_teachers(
                query
            )
        )

    def get_all_teachers(
        self,
    ):

        return (
            self.teacher_service.get_all_teachers()
        )