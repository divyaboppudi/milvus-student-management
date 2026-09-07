from rich.console import Console

console = Console()


def show_menu():

    console.print(
        "\n[bold cyan]Milvus Student Management System[/bold cyan]"
    )

    console.print("1. Create Student")
    console.print("2. View Students")
    console.print("3. Delete Student")

    console.print("4. Create Teacher")
    console.print("5. View Teachers")
    console.print("6. Delete Teacher")

    console.print("7. Create Parent")
    console.print("8. View Parents")
    console.print("9. Delete Parent")

    console.print("10. Assign Teacher To Student")
    console.print("11. Assign Parent To Student")

    console.print("12. View Relationships")

    console.print("13. Vector Search Students")
    console.print("14. Vector Search Teachers")

    console.print("15. View All Data")
    console.print("16. Delete All Data")

    console.print("0. Exit")