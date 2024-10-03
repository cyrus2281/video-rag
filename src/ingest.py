import os
from pathlib import Path
from time import sleep
import json

from config import (
    TEMP_DATA_DIR,
    DELETE_TEMP_DATA,
    METADATA_DIR,
    EXTRACTED_FRAMES_DIR,
)
from utils import (
    extract_audio_from_video,
    transcribe_audio,
    getSubs,
    extract_and_save_frames_and_metadata,
)

from embedding import get_embedded_frame
from vector_database import store_vectors


def ingest(video_path: str):
    """
    Parses and embeds the video into the vector database.
    """
    filename_no_ext = Path(video_path).stem
    audio_path = str(TEMP_DATA_DIR / (filename_no_ext + ".mp3"))
    vtt_path = str(TEMP_DATA_DIR / (filename_no_ext + ".vtt"))
    extracted_frames_path = EXTRACTED_FRAMES_DIR / filename_no_ext
    metadatas_path = METADATA_DIR / filename_no_ext
    metadata_with_embeddings_path = METADATA_DIR / (filename_no_ext + ".json")
    
    print(f"Processing video: {video_path}")

    print("Extracting audio from video...")
    extract_audio_from_video(video_path, audio_path)

    print("Transcribing audio...")
    transcribe = transcribe_audio(audio_path)

    print("Extracting VTT...")
    vtt = getSubs(transcribe["segments"], "vtt")
    # write transcription to file
    with open(vtt_path, "w") as f:
        f.write(vtt)

    # create these output folders if not existing
    Path(extracted_frames_path).mkdir(parents=True, exist_ok=True)
    Path(metadatas_path).mkdir(parents=True, exist_ok=True)

    print("Extracting frames and metadatas...")
    # call the function to extract frames and metadatas
    metadatas = extract_and_save_frames_and_metadata(
        video_path,
        vtt_path,
        str(extracted_frames_path),
        str(metadatas_path),
    )
    
    print("Embedding frames...")
    all_embeddings = []
    
    had_success = False
    start_index = 0
    while True:
        try:
            had_success = False
            for metadata in metadatas[start_index:]:
                all_embeddings.append(get_embedded_frame(metadata))
                had_success = True
                start_index += 1
            break
        except Exception as e:
            if had_success:
                # Hit rate limit, wait for a minute
                sleep(60)
                print("Embedding frame failed, waiting for a minute before retrying")
                continue
            else:
                raise e

    with open(str(metadata_with_embeddings_path), "w") as f:
        json.dump(all_embeddings, f)
        
    print("Storing embeddings...")
    all_frame_embeddings = [i[2] for i in all_embeddings]
    all_metadatas = [i[3] for i in all_embeddings]
    all_docs = [f"{i[3]['video_path']}/{i[3]['video_segment_id']}" for i in all_embeddings]
    
    store_vectors(
        all_frame_embeddings,
        all_docs,
        metadatas=all_metadatas,
    )
    
    print("Ingestion complete")

    if DELETE_TEMP_DATA:
        os.remove(audio_path)
        os.remove(vtt_path)
        os.remove(metadata_with_embeddings_path)
