def build_teacher_summary_prompt(
    teacher_data: dict,
) -> str:

    name = teacher_data.get(
        "name",
        "Unknown",
    )

    department = teacher_data.get(
        "department",
        "Unknown",
    )

    subjects = teacher_data.get(
        "subjects",
        [],
    )

    subjects_text = ", ".join(
        subjects
    )

    return f"""
Generate a professional teacher summary.

Teacher Name: {name}
Department: {department}
Subjects: {subjects_text}

Keep the summary concise and professional.
"""