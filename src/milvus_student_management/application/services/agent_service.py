from milvus_student_management.application.services.ai_service import (
    AIService,
)

from milvus_student_management.infrastructure.ai.agents.student_agent import (
    StudentAgent,
)

from milvus_student_management.infrastructure.ai.agents.teacher_agent import (
    TeacherAgent,
)

from milvus_student_management.infrastructure.ai.agents.parent_agent import (
    ParentAgent,
)

from milvus_student_management.infrastructure.ai.agents.relationship_agent import (
    RelationshipAgent,
)


class AgentService:

    def __init__(
        self,
        ai_service: AIService,
        student_agent: StudentAgent = None,
        teacher_agent: TeacherAgent = None,
        parent_agent: ParentAgent = None,
        relationship_agent: RelationshipAgent = None,
    ):
        self.ai_service = ai_service

        self.student_agent = student_agent

        self.teacher_agent = teacher_agent

        self.parent_agent = parent_agent

        self.relationship_agent = (
            relationship_agent
        )

    async def ask(
        self,
        question: str,
    ):

        question_lower = (
            question.lower()
        )

        if (
            "get student details for"
            in question_lower
        ):
            student_id = (
                question.split(
                    "for"
                )[-1].strip()
            )

            return (
                self.student_agent.get_student_details(
                    student_id
                )
            )

        if (
            "get teacher details for"
            in question_lower
        ):
            teacher_id = (
                question.split(
                    "for"
                )[-1].strip()
            )

            return (
                self.teacher_agent.get_teacher_details(
                    teacher_id
                )
            )

        if (
            "get parent details for"
            in question_lower
        ):
            parent_id = (
                question.split(
                    "for"
                )[-1].strip()
            )

            return (
                self.parent_agent.get_parent_details(
                    parent_id
                )
            )

        if (
            "get relationship details for"
            in question_lower
        ):
            relationship_id = (
                question.split(
                    "for"
                )[-1].strip()
            )

            return (
                self.relationship_agent.get_relationship_details(
                    relationship_id
                )
            )

        return await self.ai_service.generate_text(
            question
        )