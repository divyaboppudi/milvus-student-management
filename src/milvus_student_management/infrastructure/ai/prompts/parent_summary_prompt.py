def build_parent_summary_prompt(
    parent_data: dict,
) -> str:

    name = parent_data.get(
        "name",
        "Unknown",
    )

    phone_number = parent_data.get(
        "phone_number",
        "Unknown",
    )

    return f"""
Generate a professional parent summary.

Parent Name: {name}
Phone Number: {phone_number}

Keep the summary concise and professional.
"""