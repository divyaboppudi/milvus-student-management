# ==========================================
# Collection Names
# ==========================================

STUDENTS_COLLECTION = (
    "students"
)

TEACHERS_COLLECTION = (
    "teachers"
)

PARENTS_COLLECTION = (
    "parents"
)

RELATIONSHIPS_COLLECTION = (
    "relationships"
)

# ==========================================
# Embedding Configuration
# ==========================================

EMBEDDING_MODEL = (
    "sentence-transformers/all-MiniLM-L6-v2"
)

VECTOR_DIMENSION = 384

# ==========================================
# Milvus Configuration
# ==========================================

MILVUS_HOST = "localhost"

MILVUS_PORT = "19530"

# ==========================================
# Search Configuration
# ==========================================

TOP_K = 10