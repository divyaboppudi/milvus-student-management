from pymilvus import Collection

from milvus_student_management.domain.entities.student import Student
from milvus_student_management.infrastructure.embeddings.embedding_provider import (
    EmbeddingProvider,
)
from milvus_student_management.shared.constants import (
    EDUCATION_ENTITIES_COLLECTION,
)


class StudentRepository:

    def __init__(self):
        self.collection = Collection(
            EDUCATION_ENTITIES_COLLECTION
        )
        self.embedding_provider = EmbeddingProvider()

    def create(
        self,
        student: Student,
    ):

        text = (
            self.embedding_provider.create_student_text(
                student.name,
                student.grade,
                student.subjects,
            )
        )

        embedding = (
            self.embedding_provider.generate_embedding(
                text
            )
        )

        data = [
            [student.id],
            [student.entity_type.value],
            [student.model_dump()],
            [embedding],
        ]

        self.collection.insert(data)

        return student.id

    def get_by_id(
        self,
        student_id: str,
    ):

        self.collection.load()

        result = self.collection.query(
            expr=f'id == "{student_id}"',
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

        return self.collection.query(
            expr='entity_type == "student"',
            output_fields=[
                "id",
                "entity_type",
                "payload",
            ],
        )

    def update(
        self,
        student: Student,
    ):

        self.delete(student.id)
        self.create(student)

        return True

    def delete(
        self,
        student_id: str,
    ):

        self.collection.delete(
            expr=f'id == "{student_id}"'
        )

        return True

    def search_similar_students(
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

        return self.collection.search(
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