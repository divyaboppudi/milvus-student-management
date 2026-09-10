from milvus_student_management.shared.config import (
    Config,
)

from milvus_student_management.infrastructure.ai.providers.azure_provider import (
    AzureProvider,
)


class ProviderFactory:

    @staticmethod
    def create():

        provider = (
            Config.AI_PROVIDER.lower()
        )

        if provider == "azure":
            return AzureProvider()

        raise ValueError(
            f"Unsupported provider: {provider}"
        )