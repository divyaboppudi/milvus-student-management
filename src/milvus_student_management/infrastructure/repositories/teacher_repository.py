from pymilvus import Collection

from milvus_student_management.domain.entities.teacher import Teacher
from milvus_student_management.infrastructure.embeddings.embedding_provider import (
    EmbeddingProvider,
)
from milvus_student_management.shared.constants import (
    TEACHERS_COLLECTION,
)


class TeacherRepository:

    def __init__(self):
        self.collection = Collection(
            TEACHERS_COLLECTION
        )
        self.embedding_provider = EmbeddingProvider()

    def create(
        self,
        teacher: Teacher,
    ):

        text = (
            self.embedding_provider.create_teacher_text(
                teacher.name,
                teacher.department,
                teacher.subjects,
            )
        )

        embedding = (
            self.embedding_provider.generate_embedding(
                text
            )
        )

        data = [
            [teacher.id],
            [teacher.entity_type.value],
            [teacher.model_dump()],
            [embedding],
        ]

        self.collection.insert(data)

        return teacher.id

    def get_by_id(
        self,
        teacher_id: str,
    ):

        self.collection.load()

        result = self.collection.query(
            expr=f'id == "{teacher_id}"',
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

        active_teachers = []

        for result in results:

            payload = result.get(
                "payload",
                {}
            )

            if not payload.get(
                "is_deleted",
                False
            ):
                active_teachers.append(
                    result
                )

        return active_teachers

    def update(
        self,
        teacher: Teacher,
    ):

        self.delete(teacher.id)
        self.create(teacher)

        return True

    def delete(
        self,
        teacher_id: str,
    ):

        self.collection.delete(
            expr=f'id == "{teacher_id}"'
        )

        return True

    def search_similar_teachers(
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