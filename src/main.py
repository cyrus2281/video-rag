import sys
import os
from dotenv import load_dotenv

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from ingest import ingest
from search import search
from reset import reset

def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError("Please provide a command, Sollysaurus can only eat, spit, and forget")

        command = sys.argv[1]

        if command == "eat":
            if len(sys.argv) < 3:
                raise ValueError("Please provide a video path")
            video_path = sys.argv[2]
            ingest(video_path=video_path)
            
        elif command == "spit":
            if len(sys.argv) < 3:
                raise ValueError("Please provide a search query")
            search_query = " ".join(sys.argv[2:])
            search(search_query)

        elif command == "forget":
            reset()

        else:
            raise ValueError("Unknown command, Sollysaurus can only eat, spit, and forget" + command)
    except Exception as e:
        print("Error: ", e)
        sys.exit(1)
    
if __name__ == "__main__":
    main()