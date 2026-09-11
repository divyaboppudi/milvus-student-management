import requests

from milvus_student_management.infrastructure.ai.providers.base_provider import (
    BaseProvider,
)


class OllamaProvider(
    BaseProvider,
):

    async def generate(
        self,
        prompt: str,
    ) -> str:

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False,
            },
            timeout=60,
        )

        response.raise_for_status()

        data = response.json()

        return data[
            "response"
        ]