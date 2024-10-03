"""
Jina embedding https://jina.ai/embeddings
"""

import os
from langchain_community.embeddings import JinaEmbeddings

from utils import element_wise_sum

embedding_function = None
"""
Jina multi-modal embedding model instance
"""


def create_embedding_function():
    """
    Create the Jina multi-modal embedding model
    """
    global embedding_function
    api_key = os.getenv("JINA_API_KEY")

    if api_key is None:
        raise ValueError("Jina API key is missing")

    embedding_function = JinaEmbeddings(jina_api_key=api_key, model_name="jina-clip-v1")


def get_embedding_model():
    """
    Get the Jina multi-modal embedding model
    """
    global embedding_function
    if embedding_function is None:
        create_embedding_function()
    return embedding_function


def get_embedded_text(text: str):
    """
    Get the embedding for the given text
    """
    return get_embedding_model().embed_query(text)


def get_embedded_image(image_path: str):
    """
    Get the embedding for the given image
    """
    return get_embedding_model().embed_images([image_path])[0]


def get_embedded_frame(frame_metadata):
    """
    Get the embeddings for the given frame metadata
    """
    image_embedding = get_embedded_image(frame_metadata["extracted_frame_path"])
    text_embedding = get_embedded_text(frame_metadata["transcript"])
    combined_embedding = element_wise_sum(image_embedding, text_embedding)
    return image_embedding, text_embedding, combined_embedding, frame_metadata
