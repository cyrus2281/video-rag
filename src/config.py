import pathlib


DATA_DIR = pathlib.Path('data')
"""
Data directory
"""
DATA_DIR.mkdir(exist_ok=True, parents=True)

TEMP_DATA_DIR = DATA_DIR / 'temp'
"""
Temporary data directory
"""
TEMP_DATA_DIR.mkdir(exist_ok=True, parents=True)

METADATA_DIR = TEMP_DATA_DIR / 'metadatas'
"""
Metadata directory
"""

EXTRACTED_FRAMES_DIR = TEMP_DATA_DIR / 'extracted_frames'
"""
Extracted frames directory
"""

RETRIEVED_CLIPS_DIR = TEMP_DATA_DIR / 'retrieved_clips'
"""
Retrieved clips directory
"""

VDB_COLLECTION_NAME = 'vdb_rag'
"""
Vector database collection name
"""

VDB_PERSIST_DIR = str(DATA_DIR / 'chroma_langchain_db')
"""
Vector database persist directory
"""


DELETE_TEMP_DATA = False
"""
Delete temporary data after processing
"""