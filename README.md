# RAG Learning

A lightweight RAG document processing pipeline built with Python.

## Features

- Support TXT / Markdown / PDF documents
- Document data modeling
- Text cleaning
- Text chunking with overlap
- JSON export

## Architecture
Document
|
v
Loader
|
v
Cleaner
|
v
Splitter
|
v
Chunk

## Project Structure


src/
└── rag_app/
├── loader.py
├── cleaner.py
├── splitter.py
├── models.py
└── main.py


## Environment

Python 3.12

Install dependencies:

```bash
pip install -r requirements.txt

Run:

python -m src.rag_app.main