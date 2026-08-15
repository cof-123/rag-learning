from pathlib import Path

from src.rag_app.cleaner import clean_pdf_text
from src.rag_app.loader import load_pdf
from src.rag_app.models import Document
from src.rag_app.splitter import split_document_by_structure


pdf_path = Path(
    "docs/京东集团员工手册_2018.pdf"
)

raw_text = load_pdf(pdf_path)

cleaned_text = clean_pdf_text(
    raw_text
)

document = Document(
    title=pdf_path.stem,
    source=pdf_path.as_posix(),
    file_type=".pdf",
    content=cleaned_text,
    character_count=len(cleaned_text),
)

chunks = split_document_by_structure(
    document,
    max_chunk_size=400,
)

print(
    f"Chunk 数量: {len(chunks)}"
)


keywords = [
    "9:00-18:00",
    "商务宴请",
]

for keyword in keywords:
    print()
    print("=" * 80)
    print(f"关键词: {keyword}")
    print("=" * 80)

    for chunk in chunks:
        if keyword in chunk.content:
            print(
                f"Chunk ID: {chunk.chunk_id}"
            )
            print(
                f"长度: {len(chunk.content)}"
            )
            print(
                chunk.content
            )
            print("-" * 80)