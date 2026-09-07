from pymilvus import connections

from milvus_student_management.shared.constants import (
    MILVUS_HOST,
    MILVUS_PORT,
)


class MilvusConnection:

    @staticmethod
    def connect():
        connections.connect(
            alias="default",
            host=MILVUS_HOST,
            port=MILVUS_PORT,
        )

    @staticmethod
    def disconnect():
        connections.disconnect(
            "default"
        )