from pymilvus import Collection

from milvus_student_management.domain.entities.parent import Parent
from milvus_student_management.infrastructure.embeddings.embedding_provider import (
    EmbeddingProvider,
)
from milvus_student_management.shared.constants import (
    PARENTS_COLLECTION,
)


class ParentRepository:

    def __init__(self):
        self.collection = Collection(
            PARENTS_COLLECTION
        )
        self.embedding_provider = EmbeddingProvider()

    def create(
        self,
        parent: Parent,
    ):

        text = (
            self.embedding_provider.create_parent_text(
                parent.name,
                parent.phone_number,
            )
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
    ):

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

    def get_all(self):

        self.collection.load()

        results = self.collection.query(
            expr='id != ""',
            output_fields=[
                "id",
                "entity_type",
                "payload",
            ],
        )

        active_parents = []

        for result in results:

            payload = result.get(
                "payload",
                {}
            )

            if not payload.get(
                "is_deleted",
                False
            ):
                active_parents.append(
                    result
                )

        return active_parents

    def update(
        self,
        parent: Parent,
    ):

        self.delete(parent.id)
        self.create(parent)

        return True

    def delete(
        self,
        parent_id: str,
    ):

        self.collection.delete(
            expr=f'id == "{parent_id}"'
        )

        return True

    def search_similar_parents(
        self,
        query: str,
        top_k: int = 10,
    ):

        self.collection.load()

        query_embedding = (
            self.embedding_provider.generate_embedding(
                query
            )
        )

        search_params = {
            "metric_type": "COSINE",
            "params": {
                "ef": 64,
            },
        }

        results = self.collection.search(
            data=[query_embedding],
            anns_field="embedding",
            param=search_params,
            limit=top_k,
            output_fields=[
                "id",
                "entity_type",
                "payload",
            ],
        )

        filtered_results = []

        for hits in results:

            for hit in hits:

                entity = hit.entity

                payload = entity.get(
                    "payload",
                    {}
                )

                if payload.get(
                    "is_deleted",
                    False,
                ):
                    continue

                if hit.distance < 0.20:
                    continue

                filtered_results.append(
                    {
                        "id": hit.id,
                        "distance": hit.distance,
                        "entity": entity,
                    }
                )

        return filtered_results