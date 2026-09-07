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