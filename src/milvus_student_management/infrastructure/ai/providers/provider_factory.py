from milvus_student_management.shared.config import (
    Config,
)

from milvus_student_management.infrastructure.ai.providers.azure_provider import (
    AzureProvider,
)

from milvus_student_management.infrastructure.ai.providers.ollama_provider import (
    OllamaProvider,
)


class ProviderFactory:

    @staticmethod
    def create():

        print(
            "================================================"
        )

        print(
            f"AI Provider Selected: {Config.AI_PROVIDER}"
        )

        print(
            "================================================"
        )

        if Config.AI_PROVIDER == "ollama":
            return OllamaProvider()

        return AzureProvider()