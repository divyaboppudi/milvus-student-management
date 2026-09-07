from enum import Enum


class RelationshipType(str, Enum):
    TEACHES = "teaches"
    PARENT_OF = "parent_of"