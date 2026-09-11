from typing import TypedDict

from langgraph.graph import (
    END,
    StateGraph,
)


class GraphState(
    TypedDict
):
    question: str
    route: str
    entity_id: str
    response: object


class LangGraphService:

    def __init__(
        self,
        student_agent,
        teacher_agent,
        parent_agent,
        relationship_agent,
    ):
        self.student_agent = student_agent
        self.teacher_agent = teacher_agent
        self.parent_agent = parent_agent
        self.relationship_agent = relationship_agent

        graph = StateGraph(
            GraphState
        )

        graph.add_node(
            "router",
            self.router_node,
        )

        graph.add_node(
            "student",
            self.student_node,
        )

        graph.add_node(
            "teacher",
            self.teacher_node,
        )

        graph.add_node(
            "parent",
            self.parent_node,
        )

        graph.add_node(
            "relationship",
            self.relationship_node,
        )

        graph.set_entry_point(
            "router"
        )

        graph.add_conditional_edges(
            "router",
            self.route,
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

        self.graph = graph.compile()

    def router_node(
        self,
        state,
    ):
        parts = (
            state["question"]
            .split()
        )

        if len(parts) > 0:
            state["entity_id"] = (
                parts[-1]
            )

        return state

    def route(
        self,
        state,
    ):
        question = (
            state["question"]
            .lower()
        )

        if "student" in question:
            return "student"

        if "teacher" in question:
            return "teacher"

        if "parent" in question:
            return "parent"

        return "relationship"

    def student_node(
        self,
        state,
    ):
        state["response"] = (
            self.student_agent.get_student_details(
                state["entity_id"]
            )
        )

        return state

    def teacher_node(
        self,
        state,
    ):
        state["response"] = (
            self.teacher_agent.get_teacher_details(
                state["entity_id"]
            )
        )

        return state

    def parent_node(
        self,
        state,
    ):
        state["response"] = (
            self.parent_agent.get_parent_details(
                state["entity_id"]
            )
        )

        return state

    def relationship_node(
        self,
        state,
    ):
        state["response"] = (
            self.relationship_agent.get_relationship_details(
                state["entity_id"]
            )
        )

        return state

    async def ask(
        self,
        question: str,
    ):
        return self.graph.invoke(
            {
                "question": question,
                "route": "",
                "entity_id": "",
                "response": "",
            }
        )