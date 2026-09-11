from typing import TypedDict

from langgraph.graph import (
    END,
    StateGraph,
)

from milvus_student_management.application.services.ai_service import (
    AIService,
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
        ai_service: AIService,
        student_agent,
        teacher_agent,
        parent_agent,
        relationship_agent,
    ):
        self.ai_service = ai_service

        self.student_agent = student_agent
        self.teacher_agent = teacher_agent
        self.parent_agent = parent_agent
        self.relationship_agent = (
            relationship_agent
        )

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
        return state

    def route(
        self,
        state,
    ):
        return state["route"]

    async def determine_route(
        self,
        question: str,
    ):
        prompt = f"""
You are a classifier.

Respond with ONLY ONE WORD.

Allowed values:

student
teacher
parent
relationship
unknown

Do not explain.
Do not write sentences.

Question:
{question}
"""

        response = await (
            self.ai_service.generate_text(
                prompt
            )
        )

        response = (
            response
            .strip()
            .lower()
        )

        print(
            f"CLASSIFIER RESPONSE: {response}"
        )

        if response == "student":
            return "student"

        if response == "teacher":
            return "teacher"

        if response == "parent":
            return "parent"

        if response == "relationship":
            return "relationship"

        return "unknown"

    def student_node(
        self,
        state,
    ):
        question = (
            state["question"]
            .lower()
        )

        if "all" in question:
            state["response"] = (
                self.student_agent.get_all_students()
            )
        else:
            state["response"] = (
                "Please provide a student id."
            )

        return state

    def teacher_node(
        self,
        state,
    ):
        question = (
            state["question"]
            .lower()
        )

        if "all" in question:
            state["response"] = (
                self.teacher_agent.get_all_teachers()
            )
        else:
            state["response"] = (
                "Please provide a teacher id."
            )

        return state

    def parent_node(
        self,
        state,
    ):
        question = (
            state["question"]
            .lower()
        )

        if "all" in question:
            state["response"] = (
                self.parent_agent.get_all_parents()
            )
        else:
            state["response"] = (
                "Please provide a parent id."
            )

        return state

    def relationship_node(
        self,
        state,
    ):
        question = (
            state["question"]
            .lower()
        )

        if "all" in question:
            state["response"] = (
                self.relationship_agent.get_all_relationships()
            )
        else:
            state["response"] = (
                "Please provide a relationship id."
            )

        return state

    async def ask(
        self,
        question: str,
    ):
        route = await (
            self.determine_route(
                question
            )
        )

        if route == "unknown":
            return {
                "question": question,
                "response":
                "I can currently help only with students, teachers, parents and relationships."
            }

        return self.graph.invoke(
            {
                "question": question,
                "route": route,
                "entity_id": "",
                "response": "",
            }
        )