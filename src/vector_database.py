import uuid
from langchain_chroma import Chroma

from src.embedding import get_embedding_model, get_embedded_text
from src.config import VDB_COLLECTION_NAME, VDB_PERSIST_DIR

vector_store = None
"""
ChromaDB vector database instance
"""


def create_vector_database():
    """
    Create a new ChromaDB vector database instance
    """
    global vector_store
    embedding_function = get_embedding_model()
    vector_store = Chroma(
        collection_name=VDB_COLLECTION_NAME,
        embedding_function=embedding_function,
        persist_directory=VDB_PERSIST_DIR,
        collection_metadata={"hnsw:space": "cosine"},  # cosine, ip, l2
    )


def get_vector_database():
    """
    Get the ChromaDB vector database instance
    """
    global vector_store
    if vector_store is None:
        create_vector_database()
    return vector_store


def store_vectors(vectors, values, metadatas=None, ids=None):
    """
    Add vectors to the vector database
    """
    vector_store = get_vector_database()
    ids = ids or [str(uuid.uuid4()) for _ in vectors]
    vector_store._collection.upsert(
        embeddings=vectors,
        documents=values,
        metadatas=metadatas,
        ids=ids,
    )


def search_vector_database(query:str, top_k=5):
    """
    Search the vector database for the given query
    """
    vector_store = get_vector_database()
    embedded_query = get_embedded_text(query)
    results = vector_store.similarity_search_by_vector_with_relevance_scores(
        embedding=embedded_query, k=top_k
    )
    return results


def reset_vector_database():
    """
    Reset the vector database
    """
    vector_store = get_vector_database()
    vector_store.reset_collection()
    
    