# ==========================================
# Collection Names
# ==========================================

EDUCATION_ENTITIES_COLLECTION = (
    "education_entities"
)

EDUCATION_RELATIONSHIPS_COLLECTION = (
    "education_relationships"
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