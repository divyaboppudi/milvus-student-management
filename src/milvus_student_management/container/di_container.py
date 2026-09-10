from dependency_injector import containers
from dependency_injector import providers

from milvus_student_management.application.services.student_service import (
    StudentService,
)
from milvus_student_management.application.services.teacher_service import (
    TeacherService,
)
from milvus_student_management.application.services.parent_service import (
    ParentService,
)
from milvus_student_management.application.services.relationship_service import (
    RelationshipService,
)
from milvus_student_management.application.services.ai_service import (
    AIService,
)
from milvus_student_management.application.services.agent_service import (
    AgentService,
)

from milvus_student_management.infrastructure.repositories.student_repository import (
    StudentRepository,
)
from milvus_student_management.infrastructure.repositories.teacher_repository import (
    TeacherRepository,
)
from milvus_student_management.infrastructure.repositories.parent_repository import (
    ParentRepository,
)
from milvus_student_management.infrastructure.repositories.relationship_repository import (
    RelationshipRepository,
)

from milvus_student_management.infrastructure.ai.tools.student_tool import (
    StudentTool,
)
from milvus_student_management.infrastructure.ai.tools.teacher_tool import (
    TeacherTool,
)
from milvus_student_management.infrastructure.ai.tools.parent_tool import (
    ParentTool,
)
from milvus_student_management.infrastructure.ai.tools.relationship_tool import (
    RelationshipTool,
)

from milvus_student_management.infrastructure.ai.agents.student_agent import (
    StudentAgent,
)


class Container(containers.DeclarativeContainer):

    student_repository = providers.Singleton(
        StudentRepository
    )

    teacher_repository = providers.Singleton(
        TeacherRepository
    )

    parent_repository = providers.Singleton(
        ParentRepository
    )

    relationship_repository = providers.Singleton(
        RelationshipRepository
    )

    student_service = providers.Factory(
        StudentService,
        repository=student_repository,
    )

    teacher_service = providers.Factory(
        TeacherService,
        repository=teacher_repository,
    )

    parent_service = providers.Factory(
        ParentService,
        repository=parent_repository,
    )

    relationship_service = providers.Factory(
        RelationshipService,
        repository=relationship_repository,
    )

    ai_service = providers.Singleton(
        AIService,
    )

    agent_service = providers.Singleton(
        AgentService,
        ai_service=ai_service,
    )

    student_tool = providers.Factory(
        StudentTool,
        student_service=student_service,
    )

    teacher_tool = providers.Factory(
        TeacherTool,
        teacher_service=teacher_service,
    )

    parent_tool = providers.Factory(
        ParentTool,
        parent_service=parent_service,
    )

    relationship_tool = providers.Factory(
        RelationshipTool,
        relationship_service=relationship_service,
    )

    student_agent = providers.Factory(
        StudentAgent,
        student_tool=student_tool,
        relationship_tool=relationship_tool,
        parent_tool=parent_tool,
    )