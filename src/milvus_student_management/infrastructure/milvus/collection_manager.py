from pymilvus import Collection, utility

from milvus_student_management.infrastructure.milvus.schema import (
    MilvusSchemas,
)

from milvus_student_management.shared.constants import (
    STUDENTS_COLLECTION,
    TEACHERS_COLLECTION,
    PARENTS_COLLECTION,
    RELATIONSHIPS_COLLECTION,
)


class CollectionManager:

    @staticmethod
    def create_collections():

        if not utility.has_collection(
            STUDENTS_COLLECTION
        ):
            Collection(
                name=STUDENTS_COLLECTION,
                schema=MilvusSchemas.entity_schema(),
            )

        if not utility.has_collection(
            TEACHERS_COLLECTION
        ):
            Collection(
                name=TEACHERS_COLLECTION,
                schema=MilvusSchemas.entity_schema(),
            )

        if not utility.has_collection(
            PARENTS_COLLECTION
        ):
            Collection(
                name=PARENTS_COLLECTION,
                schema=MilvusSchemas.entity_schema(),
            )

        if not utility.has_collection(
            RELATIONSHIPS_COLLECTION
        ):
            Collection(
                name=RELATIONSHIPS_COLLECTION,
                schema=MilvusSchemas.relationship_schema(),
            )

    @staticmethod
    def load_collections():

        Collection(
            STUDENTS_COLLECTION
        ).load()

        Collection(
            TEACHERS_COLLECTION
        ).load()

        Collection(
            PARENTS_COLLECTION
        ).load()

        Collection(
            RELATIONSHIPS_COLLECTION
        ).load()