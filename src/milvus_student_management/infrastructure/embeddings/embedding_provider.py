import requests


class EmbeddingProvider:

    def __init__(self):
        self.model = (
            "nomic-embed-text"
        )

    def generate_embedding(
        self,
        text: str,
    ):

        response = requests.post(
            "http://localhost:11434/api/embeddings",
            json={
                "model": self.model,
                "prompt": text,
            },
            timeout=60,
        )

        response.raise_for_status()

        data = response.json()

        # Milvus collection expects 384 dimensions
        return data["embedding"][:384]

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
