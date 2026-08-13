from pathlib import Path
from .cleaner import clean_text
from .exporter import save_documents_as_json
from .loader import find_documents, load_text
from .models import Document
from dataclasses import asdict
from .splitter import split_document
from .chunk_exporter import save_chunks_as_json
from .embedding import EmbeddingModel, embed_chunks
from .vector_store import VectorStore
from .retriever import Retriever
from .chunk_loader import load_chunks_from_json



def build_document(file_path: Path) -> Document:
    """读取、清洗并构造统一文档结构。"""
    raw_text = load_text(file_path)
    cleaned_text = clean_text(raw_text)

    return Document(
        title=file_path.stem,
        source=file_path.as_posix(),
        file_type=file_path.suffix.lower(),
        content=cleaned_text,
        character_count=len(cleaned_text),
    )
def build_knowledge_base() -> None:
    """从 docs 构建并保存向量知识库。"""

    source_directory = Path("docs")

    file_paths = find_documents(
        source_directory
    )

    documents: list[Document] = []
    all_chunks = []

    for file_path in file_paths:
        try:
            document = build_document(
                file_path
            )

            documents.append(
                document
            )

            chunks = split_document(
                document,
                chunk_size=200,
                overlap=50,
            )

            all_chunks.extend(
                chunks
            )

            print(
                f"[成功] {file_path}"
            )

        except (
            OSError,
            UnicodeError,
            ValueError,
        ) as error:
            print(
                f"[失败] {file_path}：{error}"
            )

    embedding_model = EmbeddingModel()

    all_chunks = embed_chunks(
        all_chunks,
        embedding_model,
    )

    vector_store = VectorStore(
        dimension=len(
            all_chunks[0].embedding
        )
    )

    vector_store.add(
        all_chunks
    )

    vector_store.save(
        "output/faiss.index"
    )

    save_chunks_as_json(
        all_chunks,
        "output/chunks.json",
    )

    print(
        f"知识库构建完成，共 {len(all_chunks)} 个 Chunk"
    )

def query_knowledge_base(
    query: str,
    top_k: int = 3,
) -> None:
    """加载已有知识库并执行检索。"""

    chunks = load_chunks_from_json(
        "output/chunks.json"
    )

    vector_store = VectorStore.load(
        "output/faiss.index",
        chunks,
    )

    embedding_model = EmbeddingModel()

    retriever = Retriever(
        embedding_model,
        vector_store,
    )

    results = retriever.search(
        query,
        top_k=top_k,
    )

    for chunk in results:
        print()
        print("检索结果：")
        print(chunk.content)
