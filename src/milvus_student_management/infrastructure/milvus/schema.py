from pymilvus import (
    CollectionSchema,
    DataType,
    FieldSchema,
)

from milvus_student_management.shared.constants import (
    VECTOR_DIMENSION,
)


class MilvusSchemas:

    @staticmethod
    def entity_schema():

        fields = [

            FieldSchema(
                name="id",
                dtype=DataType.VARCHAR,
                max_length=128,
                is_primary=True,
            ),

            FieldSchema(
                name="entity_type",
                dtype=DataType.VARCHAR,
                max_length=32,
            ),

            FieldSchema(
                name="payload",
                dtype=DataType.JSON,
            ),

            FieldSchema(
                name="embedding",
                dtype=DataType.FLOAT_VECTOR,
                dim=VECTOR_DIMENSION,
            ),
        ]

        return CollectionSchema(
            fields=fields,
            description="Education Entities",
        )

    @staticmethod
    def relationship_schema():

        fields = [

            FieldSchema(
                name="id",
                dtype=DataType.VARCHAR,
                max_length=128,
                is_primary=True,
            ),

            FieldSchema(
                name="relationship_type",
                dtype=DataType.VARCHAR,
                max_length=32,
            ),

            FieldSchema(
                name="source_id",
                dtype=DataType.VARCHAR,
                max_length=128,
            ),

            FieldSchema(
                name="target_id",
                dtype=DataType.VARCHAR,
                max_length=128,
            ),

            FieldSchema(
                name="embedding",
                dtype=DataType.FLOAT_VECTOR,
                dim=VECTOR_DIMENSION,
            ),
        ]

        return CollectionSchema(
            fields=fields,
            description="Education Relationships",
        )