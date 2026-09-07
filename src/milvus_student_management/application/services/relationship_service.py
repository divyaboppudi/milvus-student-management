from milvus_student_management.domain.entities.relationship import (
    Relationship,
)

from milvus_student_management.infrastructure.repositories.relationship_repository import (
    RelationshipRepository,
)


class RelationshipService:

    def __init__(
        self,
        repository: RelationshipRepository,
    ) -> None:

        self.repository = repository

    def create_relationship(
        self,
        relationship: Relationship,
    ) -> str:

        return self.repository.create_relationship(
            relationship
        )

    def delete_relationship(
        self,
        relationship_id: str,
    ) -> bool:

        return self.repository.delete_relationship(
            relationship_id
        )

    def get_all_relationships(
        self,
    ):

        return self.repository.get_all()

    def get_teacher_students(
        self,
        teacher_id: str,
    ):

        return self.repository.get_teacher_students(
            teacher_id
        )

    def get_parent_students(
        self,
        parent_id: str,
    ):

        return self.repository.get_parent_students(
            parent_id
        )