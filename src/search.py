from pathlib import Path

from vector_database import search_vector_database
from utils import get_video_segment_from_metadata, play_video
from config import RETRIEVED_CLIPS_DIR

def search(query: str):
    """
    Searches the vector database for the given query.
    """
    print("Search query:", query)
    Path(RETRIEVED_CLIPS_DIR).mkdir(parents=True, exist_ok=True)
    print("Embedding query and searching database...")
    results = search_vector_database(query, top_k=3)
    print("Extracting most relevant clip...")
    output_path = str(RETRIEVED_CLIPS_DIR / "most_relevant_clip.mp4")
    most_relevant_clip_path = get_video_segment_from_metadata(results[0][0].metadata, 5, output_path)
    print("Most relevant clip path:", most_relevant_clip_path)
    print("Playing most relevant clip...")
    play_video(most_relevant_clip_path)
    
    