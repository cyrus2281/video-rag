# Video Retrieval Augmented Generation (VRAG) - Sollysaurus Version

Retrieval Augmented Generation For videos using multi-modal embedding models and vector databases.

This repository includes:
- CLI python app for ingesting videos and searching for segments using natural language queries
- Python notebook explaining the process in details.

## Notebook

The notebook is located in the [notebook/video_rag.ipynb](notebook/video_rag.ipynb) file.
Open the notebook in Google Colab using the button at the top of the notebook.

## CLI App

The CLI app has the following commands:
- `eat PATH` - Ingest videos into the database
- `spit QUERY` - Search for videos using a natural language query
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
python -m src.main COMMAND ARG
```

For example, to ingest a video:

```bash
python -m src.main eat ./data/video.mp4
```

To search for a video:

```bash
python -m src.main spit a person is playing guitar
```

Or you can build and install the CLI app using the following command:

```bash
python -m build
```

Create a new directory and virtual environment, then install the wheel file:

```bash
pip install PATH/TO/REPO/dist/sollysaurus-0.1.0-py3-none-any.whl
```

Then you can run the app using the following command:

```bash
sollysaurus COMMAND ARG
```