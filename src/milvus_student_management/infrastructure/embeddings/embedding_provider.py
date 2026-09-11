class EmbeddingProvider:

    def __init__(self):
        pass

    def generate_embedding(
        self,
        text: str,
    ):
        return [0.0] * 384

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