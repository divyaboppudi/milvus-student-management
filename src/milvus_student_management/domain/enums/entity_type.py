from enum import Enum


class EntityType(str, Enum):
    STUDENT = "student"
    TEACHER = "teacher"
    PARENT = "parent"
