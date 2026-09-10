import os


class Config:

    AI_PROVIDER = os.getenv(
        "AI_PROVIDER",
        "azure",
    )

    AZURE_OPENAI_ENDPOINT = os.getenv(
        "AZURE_OPENAI_ENDPOINT",
        "",
    )

    AZURE_OPENAI_API_KEY = os.getenv(
        "AZURE_OPENAI_API_KEY",
        "",
    )

    AZURE_OPENAI_DEPLOYMENT = os.getenv(
        "AZURE_OPENAI_DEPLOYMENT",
        "",
    )

    AWS_REGION = os.getenv(
        "AWS_REGION",
        "",
    )