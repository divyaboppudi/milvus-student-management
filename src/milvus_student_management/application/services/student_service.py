from milvus_student_management.domain.entities.student import Student
from milvus_student_management.infrastructure.repositories.student_repository import (
    StudentRepository,
)


class StudentService:

    def __init__(
        self,
        repository: StudentRepository,
    ):
        self.repository = repository

    def create_student(
        self,
        student: Student,
    ):
        return self.repository.create(student)

    def get_student(
        self,
        student_id: str,
    ):
        return self.repository.get_by_id(student_id)

    def get_all_students(self):
        return self.repository.get_all()

    def update_student(
        self,
        student: Student,
    ):
        return self.repository.update(student)

    def delete_student(
        self,
        student_id: str,
    ):
        return self.repository.delete(student_id)

    def search_students(
        self,
        query: str,
    ):
        return self.repository.search_similar_students(
            query
        )