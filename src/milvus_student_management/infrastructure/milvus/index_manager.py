from pymilvus import Collection

from milvus_student_management.shared.constants import (
    EDUCATION_ENTITIES_COLLECTION,
    EDUCATION_RELATIONSHIPS_COLLECTION,
)


class IndexManager:

    @staticmethod
    def create_entity_indexes():

        index_params = {
            "index_type": "HNSW",
            "metric_type": "COSINE",
            "params": {
                "M": 16,
                "efConstruction": 200,
            },
        }

        entity_collection = Collection(
            EDUCATION_ENTITIES_COLLECTION
        )

        try:
            entity_collection.create_index(
                field_name="embedding",
                index_params=index_params,
            )
        except Exception:
            pass

        relationship_collection = Collection(
            EDUCATION_RELATIONSHIPS_COLLECTION
        )

        try:
            relationship_collection.create_index(
                field_name="embedding",
                index_params=index_params,
            )
        except Exception:
            pass