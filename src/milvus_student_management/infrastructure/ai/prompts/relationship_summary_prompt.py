def build_relationship_summary_prompt(
    relationship_data: dict,
) -> str:

    relationship_type = relationship_data.get(
        "relationship_type",
        "Unknown",
    )

    source_id = relationship_data.get(
        "source_id",
        "Unknown",
    )

    target_id = relationship_data.get(
        "target_id",
        "Unknown",
    )

    return f"""
Generate a professional relationship summary.

Relationship Type: {relationship_type}
Source Id: {source_id}
Target Id: {target_id}

Keep the summary concise and professional.
"""