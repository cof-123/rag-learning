from dataclasses import dataclass


@dataclass
class Document:
    title: str
    source: str
    file_type: str
    content: str
    character_count: int
