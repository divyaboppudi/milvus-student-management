from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    END,
)


class GraphState(
    TypedDict
):
    question: str
    response: str


def router_node(
    state: GraphState,
):
    return state


def student_node(
    state: GraphState,
):
    print("Student Agent Executed")

    state["response"] = (
        "Student information returned"
    )

    return state


def teacher_node(
    state: GraphState,
):
    print("Teacher Agent Executed")

    state["response"] = (
        "Teacher information returned"
    )

    return state


def parent_node(
    state: GraphState,
):
    print("Parent Agent Executed")

    state["response"] = (
        "Parent information returned"
    )

    return state


def relationship_node(
    state: GraphState,
):
    print("Relationship Agent Executed")

    state["response"] = (
        "Relationship information returned"
    )

    return state


def route(
    state: GraphState,
):
    question = state["question"].lower()

    if "student" in question:
        return "student"

    if "teacher" in question:
        return "teacher"

    if "parent" in question:
        return "parent"

    return "relationship"


graph = StateGraph(
    GraphState
)

graph.add_node(
    "router",
    router_node,
)

graph.add_node(
    "student",
    student_node,
)

graph.add_node(
    "teacher",
    teacher_node,
)

graph.add_node(
    "parent",
    parent_node,
)

graph.add_node(
    "relationship",
    relationship_node,
)

graph.set_entry_point(
    "router"
)

graph.add_conditional_edges(
    "router",
    route,
    {
        "student": "student",
        "teacher": "teacher",
        "parent": "parent",
        "relationship": "relationship",
    },
)

graph.add_edge(
    "student",
    END,
)

graph.add_edge(
    "teacher",
    END,
)

graph.add_edge(
    "parent",
    END,
)

graph.add_edge(
    "relationship",
    END,
)

app = graph.compile()

result = app.invoke(
    {
        "question":
        "show parent details",
        "response":
        "",
    }
)

print(result)