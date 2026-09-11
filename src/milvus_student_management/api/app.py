import base64
from fastapi import UploadFile
from fastapi import File
from datetime import datetime
from fastapi import FastAPI


from milvus_student_management.domain.entities.student import Student
from milvus_student_management.domain.entities.teacher import Teacher

from milvus_student_management.api.models.student_request import StudentRequest
from milvus_student_management.api.models.student_update_request import (
    StudentUpdateRequest,
)

from milvus_student_management.api.models.teacher_request import (
    TeacherRequest,
)

from milvus_student_management.api.models.teacher_update_request import (
    TeacherUpdateRequest,
)

from milvus_student_management.application.services.student_service import (
    StudentService,
)

from milvus_student_management.application.services.teacher_service import (
    TeacherService,
)

from milvus_student_management.infrastructure.repositories.student_repository import (
    StudentRepository,
)

from milvus_student_management.infrastructure.repositories.teacher_repository import (
    TeacherRepository,
)

from milvus_student_management.infrastructure.milvus.connection import (
    MilvusConnection,
)

from milvus_student_management.infrastructure.milvus.collection_manager import (
    CollectionManager,
)

from milvus_student_management.infrastructure.milvus.index_manager import (
    IndexManager,
)
from milvus_student_management.domain.entities.parent import Parent

from milvus_student_management.api.models.parent_request import (
    ParentRequest,
)

from milvus_student_management.api.models.parent_update_request import (
    ParentUpdateRequest,
)

from milvus_student_management.application.services.parent_service import (
    ParentService,
)

from milvus_student_management.infrastructure.repositories.parent_repository import (
    ParentRepository,
)
from milvus_student_management.domain.entities.relationship import (
    Relationship,
)

from milvus_student_management.api.models.relationship_request import (
    RelationshipRequest,
)

from milvus_student_management.application.services.relationship_service import (
    RelationshipService,
)

from milvus_student_management.infrastructure.repositories.relationship_repository import (
    RelationshipRepository,
)
from milvus_student_management.application.services.ai_service import (
    AIService,
)
from milvus_student_management.api.models.agent_request import (
    AgentRequest,
)

from milvus_student_management.application.services.agent_service import (
    AgentService,
)

from milvus_student_management.infrastructure.ai.tools.student_tool import (
    StudentTool,
)

from milvus_student_management.infrastructure.ai.tools.relationship_tool import (
    RelationshipTool,
)

from milvus_student_management.infrastructure.ai.tools.parent_tool import (
    ParentTool,
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

from milvus_student_management.infrastructure.ai.tools.teacher_tool import (
    TeacherTool,
)

from milvus_student_management.api.models.base64_file_request import (
    Base64FileRequest,
)

from milvus_student_management.application.services.langgraph_service import (
    LangGraphService,
)
app = FastAPI(
    title="Milvus Student Management API",
    version="1.0.0",
)

MilvusConnection.connect()

CollectionManager.create_collections()

try:
    IndexManager.create_entity_indexes()
except Exception:
    pass

CollectionManager.load_collections()

student_repository = StudentRepository()

teacher_repository = TeacherRepository()

parent_repository = ParentRepository()

student_service = StudentService(
    student_repository
)

teacher_service = TeacherService(
    teacher_repository
)

parent_service = ParentService(
    parent_repository
)

relationship_service = RelationshipService(
    RelationshipRepository()
)
ai_service = AIService()

student_tool = StudentTool(
    student_service
)

teacher_tool = TeacherTool(
    teacher_service
)

parent_tool = ParentTool(
    parent_service
)

relationship_tool = RelationshipTool(
    relationship_service
)

student_agent = StudentAgent(
    student_tool,
    relationship_tool,
    parent_tool,
)

teacher_agent = TeacherAgent(
    teacher_tool
)

parent_agent = ParentAgent(
    parent_tool
)

relationship_agent = RelationshipAgent(
    relationship_tool
)

agent_service = AgentService(
    ai_service,
    student_agent,
    teacher_agent,
    parent_agent,
    relationship_agent,
)
langgraph_service = (
    LangGraphService(
        student_agent,
        teacher_agent,
        parent_agent,
        relationship_agent,
    )
)

@app.get(
    "/",
    tags=["System"],
)
def health():
    return {
        "status": "running",
        "message": "Milvus Student Management API"
    }


# =====================================================
# STUDENT APIS
# =====================================================

@app.post(
    "/students",
    tags=["Students"],
)
def create_student(
    request: StudentRequest,
):

    student = Student(
        name=request.name,
        grade=request.grade,
        subjects=request.subjects,
    )

    student_id = (
        student_service.create_student(
            student
        )
    )

    return {
        "student_id": student_id
    }


@app.get(
    "/students",
    tags=["Students"],
)
def get_all_students():

    return (
        student_service.get_all_students()
    )


@app.get(
    "/students/search",
    tags=["Students"],
)
def search_students(
    query: str,
):

    return (
        student_service.search_students(
            query
        )
    )


@app.get(
    "/students/{student_id}",
    tags=["Students"],
)
def get_student(
    student_id: str,
):

    return (
        student_service.get_student(
            student_id
        )
    )
@app.get(
    "/students/{student_id}/history",
    tags=["Students"],
)
def get_student_history(
    student_id: str,
):

    student = (
        student_service.get_student(
            student_id
        )
    )

    if not student:
        return {
            "message":
            "Student not found"
        }

    payload = student["payload"]

    return {
        "student_id":
        payload["id"],
        "current_version":
        payload.get(
            "row_version",
            1
        ),
        "created_at":
        payload.get(
            "created_at"
        ),
        "updated_at":
        payload.get(
            "updated_at"
        ),
        "created_by":
        payload.get(
            "created_by"
        ),
        "updated_by":
        payload.get(
            "updated_by"
        ),
    }


@app.put(
    "/students/{student_id}",
    tags=["Students"],
)
def update_student(
    student_id: str,
    request: StudentUpdateRequest,
):

    existing = (
        student_service.get_student(
            student_id
        )
    )

    if not existing:
        return {
            "message":
            "Student not found"
        }

    student = Student(
        **existing["payload"]
    )

    if request.row_version != student.row_version:
        return {
            "message":
            "Record modified by another user",
            "current_version":
            student.row_version
        }

    student.name = request.name
    student.grade = request.grade
    student.subjects = request.subjects

    student.row_version += 1
    student.updated_at = datetime.utcnow()
    student.updated_by = "api_user"

    student_service.update_student(
        student
    )

    return {
        "message":
        "Student updated successfully",
        "row_version":
        student.row_version,
        "updated_at":
        student.updated_at,
        "updated_by":
        student.updated_by,
    }
@app.patch(
    "/students/{student_id}",
    tags=["Students"],
)
def patch_student(
    student_id: str,
    request: StudentUpdateRequest,
):

    existing = (
        student_service.get_student(
            student_id
        )
    )

    if not existing:
        return {
            "message":
            "Student not found"
        }

    student = Student(
        **existing["payload"]
    )

    if request.row_version != student.row_version:
        return {
            "message":
            "Record modified by another user",
            "current_version":
            student.row_version
        }

    student.name = request.name
    student.grade = request.grade
    student.subjects = request.subjects

    student.row_version += 1
    student.updated_at = datetime.utcnow()
    student.updated_by = "api_user"

    student_service.update_student(
        student
    )

    return {
        "message":
        "Student patched successfully",
        "row_version":
        student.row_version,
        "updated_at":
        student.updated_at,
        "updated_by":
        student.updated_by,
    }
@app.delete(
    "/students/{student_id}",
    tags=["Students"],
)
def delete_student(
    student_id: str,
):

    student_service.delete_student(
        student_id
    )

    return {
        "message":
        "Student deleted successfully"
    }


# =====================================================
# TEACHER APIS
# =====================================================

@app.post(
    "/teachers",
    tags=["Teachers"],
)
def create_teacher(
    request: TeacherRequest,
):

    teacher = Teacher(
        name=request.name,
        department=request.department,
        subjects=request.subjects,
    )

    teacher_id = (
        teacher_service.create_teacher(
            teacher
        )
    )

    return {
        "teacher_id": teacher_id
    }


@app.get(
    "/teachers",
    tags=["Teachers"],
)
def get_all_teachers():

    return (
        teacher_service.get_all_teachers()
    )


@app.get(
    "/teachers/search",
    tags=["Teachers"],
)
def search_teachers(
    query: str,
):

    return (
        teacher_service.search_teachers(
            query
        )
    )


@app.get(
    "/teachers/{teacher_id}",
    tags=["Teachers"],
)
def get_teacher(
    teacher_id: str,
):

    return (
        teacher_service.get_teacher(
            teacher_id
        )
    )

@app.put(
    "/teachers/{teacher_id}",
    tags=["Teachers"],
)
def update_teacher(
    teacher_id: str,
    request: TeacherUpdateRequest,
):

    existing = (
        teacher_service.get_teacher(
            teacher_id
        )
    )

    if not existing:
        return {
            "message":
            "Teacher not found"
        }

    teacher = Teacher(
        **existing["payload"]
    )

    if request.row_version != teacher.row_version:
        return {
            "message":
            "Record modified by another user",
            "current_version":
            teacher.row_version
        }

    teacher.name = request.name
    teacher.department = request.department
    teacher.subjects = request.subjects

    teacher.row_version += 1
    teacher.updated_at = datetime.utcnow()
    teacher.updated_by = "api_user"

    teacher_service.update_teacher(
        teacher
    )

    return {
        "message":
        "Teacher updated successfully",
        "row_version":
        teacher.row_version,
        "updated_at":
        teacher.updated_at,
        "updated_by":
        teacher.updated_by,
    }
@app.patch(
    "/teachers/{teacher_id}",
    tags=["Teachers"],
)
def patch_teacher(
    teacher_id: str,
    request: TeacherUpdateRequest,
):

    existing = (
        teacher_service.get_teacher(
            teacher_id
        )
    )

    if not existing:
        return {
            "message":
            "Teacher not found"
        }

    teacher = Teacher(
        **existing["payload"]
    )

    if request.row_version != teacher.row_version:
        return {
            "message":
            "Record modified by another user",
            "current_version":
            teacher.row_version
        }

    teacher.name = request.name
    teacher.department = request.department
    teacher.subjects = request.subjects

    teacher.row_version += 1
    teacher.updated_at = datetime.utcnow()
    teacher.updated_by = "api_user"

    teacher_service.update_teacher(
        teacher
    )

    return {
        "message":
        "Teacher patched successfully",
        "row_version":
        teacher.row_version,
        "updated_at":
        teacher.updated_at,
        "updated_by":
        teacher.updated_by,
    }
@app.delete(
    "/teachers/{teacher_id}",
    tags=["Teachers"],
)
def delete_teacher(
    teacher_id: str,
):

    teacher_service.delete_teacher(
        teacher_id
    )

    return {
        "message":
        "Teacher deleted successfully"
    }
# =====================================================
# PARENT APIS
# =====================================================

@app.post(
    "/parents",
    tags=["Parents"],
)
def create_parent(
    request: ParentRequest,
):

    parent = Parent(
        name=request.name,
        phone_number=request.phone_number,
    )

    parent_id = (
        parent_service.create_parent(
            parent
        )
    )

    return {
        "parent_id": parent_id
    }


@app.get(
    "/parents",
    tags=["Parents"],
)
def get_all_parents():

    return (
        parent_service.get_all_parents()
    )


@app.get(
    "/parents/search",
    tags=["Parents"],
)
def search_parents(
    query: str,
):

    return (
        parent_service.search_parents(
            query
        )
    )


@app.get(
    "/parents/{parent_id}",
    tags=["Parents"],
)
def get_parent(
    parent_id: str,
):

    return (
        parent_service.get_parent(
            parent_id
        )
    )


@app.put(
    "/parents/{parent_id}",
    tags=["Parents"],
)
def update_parent(
    parent_id: str,
    request: ParentUpdateRequest,
):

    existing = (
        parent_service.get_parent(
            parent_id
        )
    )

    if not existing:
        return {
            "message":
            "Parent not found"
        }

    parent = Parent(
        **existing["payload"]
    )

    if request.row_version != parent.row_version:
        return {
            "message":
            "Record modified by another user",
            "current_version":
            parent.row_version
        }

    parent.name = request.name
    parent.phone_number = (
        request.phone_number
    )

    parent.row_version += 1
    parent.updated_at = datetime.utcnow()
    parent.updated_by = "api_user"

    parent_service.update_parent(
        parent
    )

    return {
        "message":
        "Parent updated successfully",
        "row_version":
        parent.row_version,
        "updated_at":
        parent.updated_at,
        "updated_by":
        parent.updated_by,
    }
@app.patch(
    "/parents/{parent_id}",
    tags=["Parents"],
)
def patch_parent(
    parent_id: str,
    request: ParentUpdateRequest,
):

    existing = (
        parent_service.get_parent(
            parent_id
        )
    )

    if not existing:
        return {
            "message":
            "Parent not found"
        }

    parent = Parent(
        **existing["payload"]
    )

    if request.row_version != parent.row_version:
        return {
            "message":
            "Record modified by another user",
            "current_version":
            parent.row_version
        }

    parent.name = request.name
    parent.phone_number = (
        request.phone_number
    )

    parent.row_version += 1
    parent.updated_at = datetime.utcnow()
    parent.updated_by = "api_user"

    parent_service.update_parent(
        parent
    )

    return {
        "message":
        "Parent patched successfully",
        "row_version":
        parent.row_version,
        "updated_at":
        parent.updated_at,
        "updated_by":
        parent.updated_by,
    }
@app.delete(
    "/parents/{parent_id}",
    tags=["Parents"],
)
def delete_parent(
    parent_id: str,
):

    parent_service.delete_parent(
        parent_id
    )

    return {
        "message":
        "Parent deleted successfully"
    }
# =====================================================
# RELATIONSHIP APIS
# =====================================================

@app.get(
    "/relationships",
    tags=["Relationships"],
)
def get_all_relationships():

    return (
        relationship_service.get_all_relationships()
    )


@app.get(
    "/relationships/{relationship_id}",
    tags=["Relationships"],
)
def get_relationship(
    relationship_id: str,
):

    return (
        relationship_service.get_relationship(
            relationship_id
        )
    )
@app.post(
    "/relationships",
    tags=["Relationships"],
)
def create_relationship(
    request: RelationshipRequest,
):

    relationship = Relationship(
        relationship_type=request.relationship_type,
        source_id=request.source_id,
        target_id=request.target_id,
    )

    relationship_id = (
        relationship_service.create_relationship(
            relationship
        )
    )

    return {
        "relationship_id": relationship_id
    }
@app.get(
    "/teachers/{teacher_id}/students",
    tags=["Relationships"],
)
def get_teacher_students(
    teacher_id: str,
):

    return (
        relationship_service.get_teacher_students(
            teacher_id
        )
    )


@app.get(
    "/parents/{parent_id}/students",
    tags=["Relationships"],
)
def get_parent_students(
    parent_id: str,
):

    return (
        relationship_service.get_parent_students(
            parent_id
        )
    )
@app.get(
    "/students/{student_id}/relationships",
    tags=["Relationships"],
)
def get_student_relationships(
    student_id: str,
):

    return (
        relationship_service.get_student_relationships(
            student_id
        )
    )
@app.get(
    "/stats",
    tags=["System"],
)
def get_stats():

    students = (
        student_repository.collection.query(
            expr='id != ""',
            output_fields=[
                "payload"
            ],
        )
    )

    teachers = (
        teacher_repository.collection.query(
            expr='id != ""',
            output_fields=[
                "payload"
            ],
        )
    )

    parents = (
        parent_repository.collection.query(
            expr='id != ""',
            output_fields=[
                "payload"
            ],
        )
    )

    relationships = (
        relationship_service.get_all_relationships()
    )

    active_students = sum(
        1
        for student in students
        if not student["payload"].get(
            "is_deleted",
            False
        )
    )

    deleted_students = (
        len(students)
        - active_students
    )

    active_teachers = sum(
        1
        for teacher in teachers
        if not teacher["payload"].get(
            "is_deleted",
            False
        )
    )

    deleted_teachers = (
        len(teachers)
        - active_teachers
    )

    active_parents = sum(
        1
        for parent in parents
        if not parent["payload"].get(
            "is_deleted",
            False
        )
    )

    deleted_parents = (
        len(parents)
        - active_parents
    )

    return {
        "students": {
            "total": len(students),
            "active": active_students,
            "deleted": deleted_students,
        },
        "teachers": {
            "total": len(teachers),
            "active": active_teachers,
            "deleted": deleted_teachers,
        },
        "parents": {
            "total": len(parents),
            "active": active_parents,
            "deleted": deleted_parents,
        },
        "relationships": {
            "total": len(relationships),
        },
    }


@app.delete(
    "/relationships/{relationship_id}",
    tags=["Relationships"],
)
def delete_relationship(
    relationship_id: str,
):

    relationship_service.delete_relationship(
        relationship_id
    )

    return {
        "message":
        "Relationship deleted successfully"
    }
@app.get(
    "/students/{student_id}/summary",
    tags=["AI"],
)
async def get_student_summary(
    student_id: str,
):

    student = (
        student_service.get_student(
            student_id
        )
    )

    if not student:
        return {
            "message":
            "Student not found"
        }

    payload = (
        student["payload"]
    )

    summary = (
        await ai_service.generate_student_summary(
            payload
        )
    )

    return {
        "student_id":
        payload["id"],
        "summary":
        summary,
    }
@app.get(
    "/teachers/{teacher_id}/summary",
    tags=["AI"],
)
async def get_teacher_summary(
    teacher_id: str,
):

    try:

        teacher = (
            teacher_service.get_teacher(
                teacher_id
            )
        )

        if not teacher:
            return {
                "message":
                "Teacher not found"
            }

        payload = (
            teacher["payload"]
        )

        summary = (
            await ai_service.generate_teacher_summary(
                payload
            )
        )

        return {
            "teacher_id":
            payload["id"],
            "summary":
            summary,
        }

    except Exception as ex:

        return {
            "error": str(ex)
        }
@app.get(
    "/parents/{parent_id}/summary",
    tags=["AI"],
)
async def get_parent_summary(
    parent_id: str,
):

    parent = (
        parent_service.get_parent(
            parent_id
        )
    )

    if not parent:
        return {
            "message":
            "Parent not found"
        }

    payload = (
        parent["payload"]
    )

    summary = (
        await ai_service.generate_parent_summary(
            payload
        )
    )

    return {
        "parent_id":
        payload["id"],
        "summary":
        summary,
    }
@app.get(
    "/relationships/{relationship_id}/summary",
    tags=["AI"],
)
async def get_relationship_summary(
    relationship_id: str,
):

    relationship = (
        relationship_service.get_relationship(
            relationship_id
        )
    )

    if not relationship:
        return {
            "message":
            "Relationship not found"
        }

    payload = (
        relationship["payload"]
    )

    summary = (
        await ai_service.generate_relationship_summary(
            payload
        )
    )

    return {
        "relationship_id":
        payload["id"],
        "summary":
        summary,
    }
@app.post(
    "/ai/chat",
    tags=["AI"],
)
async def chat(
    request: AgentRequest,
):

    response = (
        await agent_service.ask(
            request.question
        )
    )

    return {
        "question":
        request.question,
        "response":
        response,
    }
@app.get(
    "/ai/student-context/{student_id}",
    tags=["AI"],
)
def get_student_context(
    student_id: str,
):

    student_tool = StudentTool(
        student_service
    )

    relationship_tool = (
        RelationshipTool(
            relationship_service
        )
    )

    parent_tool = ParentTool(
        parent_service
    )

    student_agent = StudentAgent(
        student_tool,
        relationship_tool,
        parent_tool,
    )

    return (
        student_agent.get_student_context(
            student_id
        )
    )
from fastapi import UploadFile


@app.post(
    "/files/upload",
    tags=["Files"],
)
async def upload_file(
    file: UploadFile,
):

    file_path = (
        f"uploads/{file.filename}"
    )

    with open(
        file_path,
        "wb",
    ) as buffer:

        while True:

            chunk = await file.read(
                1024 * 1024
            )

            if not chunk:
                break

            buffer.write(
                chunk
            )

    return {
        "message":
        "Upload successful",
        "file_name":
        file.filename,
        "file_path":
        file_path,
    }
@app.post(
    "/images/upload",
    tags=["Files"],
)
async def upload_image(
    file: UploadFile,
):

    if not file.content_type.startswith(
        "image/"
    ):
        return {
            "message":
            "Only image files allowed"
        }

    file_path = (
        f"uploads/{file.filename}"
    )

    with open(
        file_path,
        "wb",
    ) as buffer:

        while True:

            chunk = await file.read(
                1024 * 1024
            )

            if not chunk:
                break

            buffer.write(
                chunk
            )

    return {
        "message":
        "Image uploaded successfully",
        "file_name":
        file.filename,
        "file_path":
        file_path,
    }
@app.post(
    "/files/upload-base64",
    tags=["Files"],
)
def upload_base64_file(
    request: Base64FileRequest,
):

    file_path = (
        f"uploads/{request.file_name}"
    )

    file_bytes = (
        base64.b64decode(
            request.content
        )
    )

    with open(
        file_path,
        "wb",
    ) as file:

        file.write(
            file_bytes
        )

    return {
        "message":
        "File uploaded successfully",
        "file_path":
        file_path,
    }
@app.post(
    "/langgraph/chat",
)
async def langgraph_chat(
    question: str,
):
    return await (
        langgraph_service.ask(
            question
        )
    )