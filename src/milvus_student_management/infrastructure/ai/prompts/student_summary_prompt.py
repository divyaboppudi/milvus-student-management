def build_student_summary_prompt(
    student_data: dict,
) -> str:

    name = student_data.get(
        "name",
        "Unknown",
    )

    grade = student_data.get(
        "grade",
        "Unknown",
    )

    subjects = student_data.get(
        "subjects",
        [],
    )

    subjects_text = ", ".join(
        subjects
    )

    return f"""
Generate a professional student summary.

Student Name: {name}
Grade: {grade}
Subjects: {subjects_text}

Keep the summary concise and professional.
"""