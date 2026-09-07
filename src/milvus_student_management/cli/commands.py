from milvus_student_management.domain.entities.parent import Parent
from milvus_student_management.domain.entities.relationship import Relationship
from milvus_student_management.domain.entities.student import Student
from milvus_student_management.domain.entities.teacher import Teacher
from milvus_student_management.domain.enums.relationship_type import (
    RelationshipType,
)


def create_student(student_service):

    name = input("Student Name: ")
    grade = input("Grade: ")

    subjects = input(
        "Subjects (comma separated): "
    ).split(",")

    student = Student(
        name=name,
        grade=grade,
        subjects=[
            subject.strip()
            for subject in subjects
        ],
    )

    student_id = student_service.create_student(
        student
    )

    print(f"\nStudent Created: {student_id}")


def view_students(student_service):

    students = (
        student_service.get_all_students()
    )

    if not students:
        print("\nNo student records found.")
        return

    for student in students:
        print(student)


def delete_student(student_service):

    student_id = input(
        "Student Id: "
    )

    student = (
        student_service.get_student(
            student_id
        )
    )

    if not student:
        print("\nStudent not found.")
        return

    student_service.delete_student(
        student_id
    )

    print("\nStudent Deleted")


def create_teacher(teacher_service):

    name = input("Teacher Name: ")

    department = input(
        "Department: "
    )

    subjects = input(
        "Subjects (comma separated): "
    ).split(",")

    teacher = Teacher(
        name=name,
        department=department,
        subjects=[
            s.strip()
            for s in subjects
        ],
    )

    teacher_id = (
        teacher_service.create_teacher(
            teacher
        )
    )

    print(
        f"\nTeacher Created: {teacher_id}"
    )


def view_teachers(teacher_service):

    teachers = (
        teacher_service.get_all_teachers()
    )

    if not teachers:
        print("\nNo teacher records found.")
        return

    for teacher in teachers:
        print(teacher)


def delete_teacher(teacher_service):

    teacher_id = input(
        "Teacher Id: "
    )

    teacher = (
        teacher_service.get_teacher(
            teacher_id
        )
    )

    if not teacher:
        print("\nTeacher not found.")
        return

    teacher_service.delete_teacher(
        teacher_id
    )

    print("\nTeacher Deleted")


def create_parent(parent_service):

    name = input(
        "Parent Name: "
    )

    phone_number = input(
        "Phone Number: "
    )

    parent = Parent(
        name=name,
        phone_number=phone_number,
    )

    parent_id = (
        parent_service.create_parent(
            parent
        )
    )

    print(
        f"\nParent Created: {parent_id}"
    )


def view_parents(parent_service):

    parents = (
        parent_service.get_all_parents()
    )

    if not parents:
        print("\nNo parent records found.")
        return

    for parent in parents:
        print(parent)


def delete_parent(parent_service):

    parent_id = input(
        "Parent Id: "
    )

    parent = (
        parent_service.get_parent(
            parent_id
        )
    )

    if not parent:
        print("\nParent not found.")
        return

    parent_service.delete_parent(
        parent_id
    )

    print("\nParent Deleted")


def assign_teacher_to_student(
    relationship_service,
    teacher_service,
    student_service,
):

    teacher_id = input(
        "Teacher Id: "
    )

    teacher = teacher_service.get_teacher(
        teacher_id
    )

    if not teacher:
        print("\nTeacher not found.")
        return

    student_id = input(
        "Student Id: "
    )

    student = student_service.get_student(
        student_id
    )

    if not student:
        print("\nStudent not found.")
        return

    relationship = Relationship(
        relationship_type=RelationshipType.TEACHES,
        source_id=teacher_id,
        target_id=student_id,
    )

    relationship_service.create_relationship(
        relationship
    )

    print(
        "\nTeacher assigned successfully"
    )


def assign_parent_to_student(
    relationship_service,
    parent_service,
    student_service,
):

    parent_id = input(
        "Parent Id: "
    )

    parent = parent_service.get_parent(
        parent_id
    )

    if not parent:
        print("\nParent not found.")
        return

    student_id = input(
        "Student Id: "
    )

    student = student_service.get_student(
        student_id
    )

    if not student:
        print("\nStudent not found.")
        return

    relationship = Relationship(
        relationship_type=RelationshipType.PARENT_OF,
        source_id=parent_id,
        target_id=student_id,
    )

    relationship_service.create_relationship(
        relationship
    )

    print(
        "\nParent assigned successfully"
    )


def view_relationships(
    relationship_service,
):

    relationships = (
        relationship_service.get_all_relationships()
    )

    if not relationships:
        print("\nNo relationships found.")
        return

    for relationship in relationships:
        print(relationship)


def search_students(
    student_service,
):

    query = input(
        "Search Query: "
    )

    results = (
        student_service.search_students(
            query
        )
    )

    if not results:
        print("\nNo matching students found.")
        return

    for result in results:
        print(result)


def search_teachers(
    teacher_service,
):

    query = input(
        "Search Query: "
    )

    results = (
        teacher_service.search_teachers(
            query
        )
    )

    if not results:
        print("\nNo matching teachers found.")
        return

    for result in results:
        print(result)


def view_all_data(
    student_service,
    teacher_service,
    parent_service,
    relationship_service,
):

    print("\n===== STUDENTS =====")

    students = student_service.get_all_students()

    if not students:
        print("No students found.")
    else:
        for student in students:
            print(student)

    print("\n===== TEACHERS =====")

    teachers = teacher_service.get_all_teachers()

    if not teachers:
        print("No teachers found.")
    else:
        for teacher in teachers:
            print(teacher)

    print("\n===== PARENTS =====")

    parents = parent_service.get_all_parents()

    if not parents:
        print("No parents found.")
    else:
        for parent in parents:
            print(parent)

    print("\n===== RELATIONSHIPS =====")

    relationships = relationship_service.get_all_relationships()

    if not relationships:
        print("No relationships found.")
    else:
        for relationship in relationships:
            print(relationship)


def delete_all_data(
    student_service,
    teacher_service,
    parent_service,
    relationship_service,
):

    students = student_service.get_all_students()

    for student in students:
        student_service.delete_student(
            student["id"]
        )

    teachers = teacher_service.get_all_teachers()

    for teacher in teachers:
        teacher_service.delete_teacher(
            teacher["id"]
        )

    parents = parent_service.get_all_parents()

    for parent in parents:
        parent_service.delete_parent(
            parent["id"]
        )

    relationships = (
        relationship_service.get_all_relationships()
    )

    for relationship in relationships:
        relationship_service.delete_relationship(
            relationship["id"]
        )

    print(
        "\nAll data deleted successfully."
    )