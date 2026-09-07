from milvus_student_management.domain.entities.parent import Parent
from milvus_student_management.infrastructure.repositories.parent_repository import (
    ParentRepository,
)


class ParentService:

    def __init__(
        self,
        repository: ParentRepository,
    ):
        self.repository = repository

    def create_parent(
        self,
        parent: Parent,
    ):
        return self.repository.create(parent)

    def get_parent(
        self,
        parent_id: str,
    ):
        return self.repository.get_by_id(parent_id)

    def get_all_parents(self):
        return self.repository.get_all()

    def update_parent(
        self,
        parent: Parent,
    ):
        return self.repository.update(parent)

    def delete_parent(
        self,
        parent_id: str,
    ):
        return self.repository.delete(parent_id)

    def search_parents(
        self,
        query: str,
    ):
        return self.repository.search_similar_parents(
            query
        )