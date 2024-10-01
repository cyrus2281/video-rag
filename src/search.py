from pathlib import Path

from src.vector_database import search_vector_database
from src.utils import get_video_segment_from_metadata, play_video
from src.config import RETRIEVED_CLIPS_DIR

def search(query: str):
    """
    Searches the vector database for the given query.
    """
    Path(RETRIEVED_CLIPS_DIR).mkdir(parents=True, exist_ok=True)
    print("Embedding query and searching database...")
    results = search_vector_database(query, top_k=3)
    print("Extracting most relevant clip...")
    most_relevant_clip_path = get_video_segment_from_metadata(results[0][0].metadata, 5)
    print("Most relevant clip path:", most_relevant_clip_path)
    print("Playing most relevant clip...")
    play_video(most_relevant_clip_path)
    
    