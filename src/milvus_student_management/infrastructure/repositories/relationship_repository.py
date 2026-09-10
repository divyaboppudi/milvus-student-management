from pymilvus import Collection

from milvus_student_management.domain.entities.relationship import (
    Relationship,
)

from milvus_student_management.shared.constants import (
    RELATIONSHIPS_COLLECTION,
    VECTOR_DIMENSION,
)


class RelationshipRepository:

    def __init__(self):
        self.collection = Collection(
            RELATIONSHIPS_COLLECTION
        )

    def create_relationship(
        self,
        relationship: Relationship,
    ):

        data = [
            [relationship.id],
            [relationship.relationship_type.value],
            [relationship.source_id],
            [relationship.target_id],
            [[0.0] * VECTOR_DIMENSION],
        ]

        self.collection.insert(data)

        return relationship.id

    def delete_relationship(
        self,
        relationship_id: str,
    ):

        self.collection.delete(
            expr=f'id == "{relationship_id}"'
        )

        return True

    def get_relationship_by_id(
        self,
        relationship_id: str,
    ):

        self.collection.load()

        result = self.collection.query(
            expr=f'id == "{relationship_id}"',
            output_fields=[
                "id",
                "relationship_type",
                "source_id",
                "target_id",
            ],
        )

        return result[0] if result else None

    def get_relationships_by_source(
        self,
        source_id: str,
    ):

        self.collection.load()

        return self.collection.query(
            expr=f'source_id == "{source_id}"',
            output_fields=[
                "id",
                "relationship_type",
                "source_id",
                "target_id",
            ],
        )

    def get_relationships_by_target(
        self,
        target_id: str,
    ):

        self.collection.load()

        return self.collection.query(
            expr=f'target_id == "{target_id}"',
            output_fields=[
                "id",
                "relationship_type",
                "source_id",
                "target_id",
            ],
        )

    def get_all(self):

        self.collection.load()

        return self.collection.query(
            expr='id != ""',
            output_fields=[
                "id",
                "relationship_type",
                "source_id",
                "target_id",
            ],
        )

    def get_teacher_students(
        self,
        teacher_id: str,
    ):

        self.collection.load()

        return self.collection.query(
            expr=(
                f'source_id == "{teacher_id}" and '
                f'relationship_type == "teaches"'
            ),
            output_fields=[
                "id",
                "target_id",
            ],
        )

    def get_parent_students(
        self,
        parent_id: str,
    ):

        self.collection.load()

        return self.collection.query(
            expr=(
                f'source_id == "{parent_id}" and '
                f'relationship_type == "parent_of"'
            ),
            output_fields=[
                "id",
                "target_id",
            ],
        )