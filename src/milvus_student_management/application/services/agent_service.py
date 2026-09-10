from milvus_student_management.application.services.ai_service import (
    AIService,
)


class AgentService:

    def __init__(
        self,
        ai_service: AIService,
    ):
        self.ai_service = ai_service

    async def ask(
        self,
        question: str,
    ) -> str:

        return await self.ai_service.generate_text(
            question
        )