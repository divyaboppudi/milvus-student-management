from pymilvus import Collection

from milvus_student_management.shared.constants import (
    STUDENTS_COLLECTION,
    TEACHERS_COLLECTION,
    PARENTS_COLLECTION,
    RELATIONSHIPS_COLLECTION,
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

        collections = [
            STUDENTS_COLLECTION,
            TEACHERS_COLLECTION,
            PARENTS_COLLECTION,
            RELATIONSHIPS_COLLECTION,
        ]

        for collection_name in collections:

            collection = Collection(
                collection_name
            )

            try:
                collection.create_index(
                    field_name="embedding",
                    index_params=index_params,
                )
            except Exception:
                pass
