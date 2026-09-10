from milvus_student_management.application.services.parent_service import (
    ParentService,
)


class ParentTool:

    def __init__(
        self,
        parent_service: ParentService,
    ):
        self.parent_service = (
            parent_service
        )

    def get_parent(
        self,
        parent_id: str,
    ):

        return (
            self.parent_service.get_parent(
                parent_id
            )
        )

    def search_parents(
        self,
        query: str,
    ):

        return (
            self.parent_service.search_parents(
                query
            )
        )

    def get_all_parents(
        self,
    ):

        return (
            self.parent_service.get_all_parents()
        )