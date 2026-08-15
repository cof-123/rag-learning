from .models import Chunk, Document
import re

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



def is_section_start(line: str) -> bool:
    """判断是否为章节或条款起始行。"""

    patterns = [
        r"^第[一二三四五六七八九十]+章",
        r"^第[一二三四五六七八九十]+节",
        r"^\d+\.\s",
        r"^\d+\.\d+\s",
        r"^\d+\.\d+\.\d+\s",
    ]

    return any(
        re.match(pattern, line)
        for pattern in patterns
    )

def split_document_by_structure(
    document: Document,
    max_chunk_size: int = 400,
) -> list[Chunk]:
    """优先按章节和条款结构切分文档。"""

    lines = [
        line.strip()
        for line in document.content.splitlines()
        if line.strip()
    ]

    sections: list[str] = []
    current_lines: list[str] = []

    for line in lines:
        if is_section_start(line) and current_lines:
            sections.append(
                "\n".join(current_lines)
            )
            current_lines = []

        current_lines.append(line)

    if current_lines:
        sections.append(
            "\n".join(current_lines)
        )

    chunks: list[Chunk] = []
    chunk_id = 0

    for section in sections:
        if len(section) <= max_chunk_size:
            chunks.append(
                Chunk(
                    content=section,
                    chunk_id=chunk_id,
                    source=document.source,
                )
            )
            chunk_id += 1

        else:
            start = 0

            while start < len(section):
                end = start + max_chunk_size

                chunk_text = section[
                    start:end
                ]

                chunks.append(
                    Chunk(
                        content=chunk_text,
                        chunk_id=chunk_id,
                        source=document.source,
                    )
                )

                chunk_id += 1
                start = end

    return chunks