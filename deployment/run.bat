@echo off

docker compose -f deployment/docker-compose.yml up -d

uv run python -m milvus_student_management.main