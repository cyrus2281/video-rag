import shutil
from src.config import TEMP_DATA_DIR
from src.vector_database import reset_vector_database

def reset():
    """
    Reset the vector database and clear the temporary data.
    """
    reset_vector_database()
    # recursively delete the temporary data directory
    shutil.rmtree(TEMP_DATA_DIR)
    print("Reset successful.")