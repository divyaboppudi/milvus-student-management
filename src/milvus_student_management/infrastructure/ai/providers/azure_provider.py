from milvus_student_management.infrastructure.ai.providers.base_provider import (
    BaseProvider,
)


class AzureProvider(BaseProvider):

    async def generate(
        self,
        prompt: str,
    ) -> str:

        return (
            f"Azure Provider Response: {prompt}"
        )