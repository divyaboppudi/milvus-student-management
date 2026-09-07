from abc import ABC, abstractmethod

from milvus_student_management.domain.entities.relationship import (
    Relationship,
)


class RelationshipRepositoryInterface(ABC):

    @abstractmethod
    def create_relationship(
        self,
        relationship: Relationship,
    ):
        pass

    @abstractmethod
    def delete_relationship(
        self,
        relationship_id: str,
    ):
        pass

    @abstractmethod
    def get_relationship_by_id(
        self,
        relationship_id: str,
    ):
        pass

    @abstractmethod
    def get_relationships_by_source(
        self,
        source_id: str,
    ):
        pass

    @abstractmethod
    def get_relationships_by_target(
        self,
        target_id: str,
    ):
        pass

    @abstractmethod
    def get_all(self):
        pass