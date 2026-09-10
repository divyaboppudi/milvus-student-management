from milvus_student_management.application.services.relationship_service import (
    RelationshipService,
)


class RelationshipTool:

    def __init__(
        self,
        relationship_service: RelationshipService,
    ):
        self.relationship_service = (
            relationship_service
        )

    def get_relationship(
        self,
        relationship_id: str,
    ):

        return (
            self.relationship_service.get_relationship(
                relationship_id
            )
        )

    def get_all_relationships(
        self,
    ):

        return (
            self.relationship_service.get_all_relationships()
        )

    def get_teacher_students(
        self,
        teacher_id: str,
    ):

        return (
            self.relationship_service.get_teacher_students(
                teacher_id
            )
        )

    def get_parent_students(
        self,
        parent_id: str,
    ):

        return (
            self.relationship_service.get_parent_students(
                parent_id
            )
        )

    def get_student_relationships(
        self,
        student_id: str,
    ):

        return (
            self.relationship_service.get_student_relationships(
                student_id
            )
        )