from milvus_student_management.infrastructure.ai.providers.provider_factory import (
    ProviderFactory,
)

from milvus_student_management.infrastructure.ai.prompts.student_summary_prompt import (
    build_student_summary_prompt,
)

from milvus_student_management.infrastructure.ai.prompts.teacher_summary_prompt import (
    build_teacher_summary_prompt,
)

from milvus_student_management.infrastructure.ai.prompts.parent_summary_prompt import (
    build_parent_summary_prompt,
)


class AIService:

    def __init__(self):
        self.provider = (
            ProviderFactory.create()
        )

    async def generate_text(
        self,
        prompt: str,
    ) -> str:
        return await self.provider.generate(
            prompt
        )

    async def generate_student_summary(
        self,
        student: dict,
    ) -> str:

        prompt = (
            build_student_summary_prompt(
                student
            )
        )

        return await self.provider.generate(
            prompt
        )

    async def generate_teacher_summary(
        self,
        teacher: dict,
    ) -> str:

        prompt = (
            build_teacher_summary_prompt(
                teacher
            )
        )

        return await self.provider.generate(
            prompt
        )

    async def generate_parent_summary(
        self,
        parent: dict,
    ) -> str:

        prompt = (
            build_parent_summary_prompt(
                parent
            )
        )

        return await self.provider.generate(
            prompt
        )