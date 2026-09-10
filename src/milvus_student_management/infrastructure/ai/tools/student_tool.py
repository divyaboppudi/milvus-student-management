from milvus_student_management.application.services.student_service import (
    StudentService,
)


class StudentTool:

    def __init__(
        self,
        student_service: StudentService,
    ):
        self.student_service = (
            student_service
        )

    def get_student(
        self,
        student_id: str,
    ):

        return (
            self.student_service.get_student(
                student_id
            )
        )

    def search_students(
        self,
        query: str,
    ):

        return (
            self.student_service.search_students(
                query
            )
        )

    def get_all_students(
        self,
    ):

        return (
            self.student_service.get_all_students()
        )