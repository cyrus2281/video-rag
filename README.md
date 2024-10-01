# Video Retrieval Augmented Generation (VRAG)

Retrieval Augmented Generation For videos using multi-modal embedding models and vector databases.

This repository includes:
- CLI python app for ingesting videos and searching for segments using natural language queries
- Python notebook explaining the process in details.

## Notebook

The notebook is located in the [notebook/video_rag.ipynb](notebook/video_rag.ipynb) file.
Open the notebook in Google Colab using the button at the top of the notebook.

## CLI App

The CLI app has the following commands:
- `ingest PATH` - Ingest videos into the database
- `search QUERY` - Search for videos using a natural language query
- `reset` - Reset the database

To run the app, first install the requirements.
It's recommended to use a virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then run the app using the following command:

```bash
python main.py COMMAND ARG
```

For example, to ingest a video:

```bash
python main.py ingest ./data/video.mp4
```

To search for a video:

```bash
python main.py search a person is playing guitar
```