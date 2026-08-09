from dataclasses import dataclass
from typing import Optional

@dataclass
class Document:
    title: str
    source: str
    file_type: str
    content: str
    character_count: int



@dataclass
class Chunk:
    content: str
    chunk_id: int
    source: str
    embedding: Optional[list[float]] = None