from rich.console import Console

from milvus_student_management.cli.commands import (
    assign_parent_to_student,
    assign_teacher_to_student,
    create_parent,
    create_student,
    create_teacher,
    delete_all_data,
    delete_parent,
    delete_student,
    delete_teacher,
    search_students,
    search_teachers,
    view_all_data,
    view_parents,
    view_relationships,
    view_students,
    view_teachers,
)

from milvus_student_management.cli.menu import (
    show_menu,
)

from milvus_student_management.container.di_container import (
    Container,
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

console = Console()


def main():

    MilvusConnection.connect()

    CollectionManager.create_collections()

    try:
        IndexManager.create_entity_indexes()
    except Exception:
        pass

    CollectionManager.load_collections()

    container = Container()

    student_service = (
        container.student_service()
    )

    teacher_service = (
        container.teacher_service()
    )

    parent_service = (
        container.parent_service()
    )

    relationship_service = (
        container.relationship_service()
    )

    while True:

        show_menu()

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            create_student(
                student_service
            )

        elif choice == "2":

            view_students(
                student_service
            )

        elif choice == "3":

            delete_student(
                student_service
            )

        elif choice == "4":

            create_teacher(
                teacher_service
            )

        elif choice == "5":

            view_teachers(
                teacher_service
            )

        elif choice == "6":

            delete_teacher(
                teacher_service
            )

        elif choice == "7":

            create_parent(
                parent_service
            )

        elif choice == "8":

            view_parents(
                parent_service
            )

        elif choice == "9":

            delete_parent(
                parent_service
            )

        elif choice == "10":

            assign_teacher_to_student(
                relationship_service,
                teacher_service,
                student_service,
            )

        elif choice == "11":

            assign_parent_to_student(
                relationship_service,
                parent_service,
                student_service,
            )

        elif choice == "12":

            view_relationships(
                relationship_service
            )

        elif choice == "13":

            search_students(
                student_service
            )

        elif choice == "14":

            search_teachers(
                teacher_service
            )

        elif choice == "15":

            view_all_data(
                student_service,
                teacher_service,
                parent_service,
                relationship_service,
            )

        elif choice == "16":

            delete_all_data(
                student_service,
                teacher_service,
                parent_service,
                relationship_service,
            )

        elif choice == "0":

            print(
                "\nGoodbye..."
            )

            break

        else:

            print(
                "\nInvalid Choice"
            )


if __name__ == "__main__":
    main()