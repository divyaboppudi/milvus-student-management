from milvus_student_management.domain.entities.teacher import Teacher
from milvus_student_management.infrastructure.repositories.teacher_repository import (
    TeacherRepository,
)


class TeacherService:

    def __init__(
        self,
        repository: TeacherRepository,
    ):
        self.repository = repository

    def create_teacher(
        self,
        teacher: Teacher,
    ):
        return self.repository.create(teacher)

    def get_teacher(
        self,
        teacher_id: str,
    ):
        return self.repository.get_by_id(teacher_id)

    def get_all_teachers(self):
        return self.repository.get_all()

    def update_teacher(
        self,
        teacher: Teacher,
    ):
        return self.repository.update(teacher)

    def delete_teacher(
        self,
        teacher_id: str,
    ):
        teacher_record = (
            self.repository.get_by_id(
                teacher_id
            )
        )

        if not teacher_record:
            return False

        payload = teacher_record["payload"]

        teacher = Teacher(
            **payload
        )

        teacher.is_deleted = True

        return self.repository.update(
            teacher
        )

    def search_teachers(
        self,
        query: str,
    ):
        return self.repository.search_similar_teachers(
            query
        )