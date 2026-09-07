from pymilvus import Collection, utility

from milvus_student_management.infrastructure.milvus.schema import (
    MilvusSchemas,
)

from milvus_student_management.shared.constants import (
    EDUCATION_ENTITIES_COLLECTION,
    EDUCATION_RELATIONSHIPS_COLLECTION,
)


class CollectionManager:

    @staticmethod
    def create_collections():

        if not utility.has_collection(
            EDUCATION_ENTITIES_COLLECTION
        ):
            Collection(
                name=EDUCATION_ENTITIES_COLLECTION,
                schema=MilvusSchemas.entity_schema(),
            )

        if not utility.has_collection(
            EDUCATION_RELATIONSHIPS_COLLECTION
        ):
            Collection(
                name=EDUCATION_RELATIONSHIPS_COLLECTION,
                schema=MilvusSchemas.relationship_schema(),
            )

    @staticmethod
    def load_collections():

        Collection(
            EDUCATION_ENTITIES_COLLECTION
        ).load()