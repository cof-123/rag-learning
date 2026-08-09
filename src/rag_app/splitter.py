from .models import Chunk, Document


def split_document(
    document: Document,
    chunk_size: int,
    overlap: int,
) -> list[Chunk]:
    """把Document切分成多个Chunk。"""

    chunks = []

    start = 0
    chunk_id = 0

    text = document.content

    while start < len(text):

        end = start + chunk_size

        chunk_text = text[start:end]

        chunks.append(
            Chunk(
                content=chunk_text,
                chunk_id=chunk_id,
                source=document.source,
            )
        )

        chunk_id += 1

        if end >= len(text):
            break

        start = end - overlap

    return chunks