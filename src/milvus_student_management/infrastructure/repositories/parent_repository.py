from pymilvus import Collection

from milvus_student_management.domain.entities.parent import Parent
from milvus_student_management.infrastructure.embeddings.embedding_provider import (
    EmbeddingProvider,
)
from milvus_student_management.shared.constants import (
    EDUCATION_ENTITIES_COLLECTION,
)


class ParentRepository:

    def __init__(self) -> None:

        self.collection = Collection(
            EDUCATION_ENTITIES_COLLECTION
        )

        self.embedding_provider = (
            EmbeddingProvider()
        )

    def create(
        self,
        parent: Parent,
    ) -> str:

        text = (
            f"Parent Name: {parent.name}. "
            f"Phone Number: {parent.phone_number}"
        )

        embedding = (
            self.embedding_provider.generate_embedding(
                text
            )
        )

        data = [
            [parent.id],
            [parent.entity_type.value],
            [parent.model_dump()],
            [embedding],
        ]

        self.collection.insert(data)

        return parent.id

    def get_by_id(
        self,
        parent_id: str,
    ) -> dict | None:

        self.collection.load()

        result = self.collection.query(
            expr=f'id == "{parent_id}"',
            output_fields=[
                "id",
                "entity_type",
                "payload",
            ],
        )

        if not result:
            return None

        return result[0]

    def get_all(self) -> list:

        self.collection.load()

        return self.collection.query(
            expr='entity_type == "parent"',
            output_fields=[
                "id",
                "entity_type",
                "payload",
            ],
        )

    def update(
        self,
        parent: Parent,
    ) -> bool:

        self.delete(parent.id)

        self.create(parent)

        return True

    def delete(
        self,
        parent_id: str,
    ) -> bool:

        self.collection.delete(
            expr=f'id == "{parent_id}"'
        )

        return True

    def search_similar_parents(
        self,
        query: str,
        top_k: int = 10,
    ) -> list:

        self.collection.load()

        query_embedding = (
            self.embedding_provider.generate_embedding(
                query
            )
        )

        results = self.collection.search(
            data=[query_embedding],
            anns_field="embedding",
            limit=top_k,
            output_fields=[
                "id",
                "entity_type",
                "payload",
            ],
        )

        return results