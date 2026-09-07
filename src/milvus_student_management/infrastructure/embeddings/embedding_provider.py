from sentence_transformers import SentenceTransformer

from milvus_student_management.shared.constants import (
    EMBEDDING_MODEL,
)


class EmbeddingProvider:

    def __init__(self):
        self._model = SentenceTransformer(
            EMBEDDING_MODEL
        )

    def generate_embedding(
        self,
        text: str,
    ):
        return self._model.encode(
            text,
            normalize_embeddings=True,
        ).tolist()

    def create_student_text(
        self,
        name: str,
        grade: str,
        subjects: list[str],
    ):
        return (
            f"Student Name: {name}. "
            f"Grade: {grade}. "
            f"Subjects: {' '.join(subjects)}"
        )

    def create_teacher_text(
        self,
        name: str,
        department: str,
        subjects: list[str],
    ):
        return (
            f"Teacher Name: {name}. "
            f"Department: {department}. "
            f"Subjects: {' '.join(subjects)}"
        )

    def create_parent_text(
        self,
        name: str,
        phone_number: str,
    ):
        return (
            f"Parent Name: {name}. "
            f"Phone Number: {phone_number}"
        )