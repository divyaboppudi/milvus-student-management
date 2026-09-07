class StudentManagementException(Exception):
    pass


class EntityNotFoundException(
    StudentManagementException
):
    pass


class RelationshipException(
    StudentManagementException
):
    pass


class MilvusConnectionException(
    StudentManagementException
):
    pass