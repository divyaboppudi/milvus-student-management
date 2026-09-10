import asyncio

from milvus_student_management.application.services.ai_service import (
    AIService,
)


async def main():

    ai_service = AIService()

    summary = await ai_service.generate_student_summary(
        {
            "name": "John",
            "grade": "10",
            "subjects": [
                "Math",
                "Science",
                "English",
            ],
        }
    )

    print(summary)


if __name__ == "__main__":
    asyncio.run(main())