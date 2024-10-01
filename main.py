import sys
from dotenv import load_dotenv

from src.ingest import ingest
from src.search import search
from src.reset import reset

load_dotenv()

def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError("Please provide a command")

        command = sys.argv[1]

        if command == "ingest":
            if len(sys.argv) < 3:
                raise ValueError("Please provide a video path")
            video_path = sys.argv[2]
            ingest(video_path=video_path)
            
        elif command == "search":
            if len(sys.argv) < 3:
                raise ValueError("Please provide a search query")
            search_query = " ".join(sys.argv[2:])
            search(search_query)

        elif command == "reset":
            reset()

        else:
            raise ValueError("Unknown command " + command)
    except Exception as e:
        print("Error: ", e)
        raise e
        sys.exit(1)
    
if __name__ == "__main__":
    main()