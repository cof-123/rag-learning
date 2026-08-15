from pathlib import Path
from .cleaner import (
    clean_text,
    clean_pdf_text,
)
from .exporter import save_documents_as_json
from .loader import find_documents, load_text
from .models import Document
from dataclasses import asdict
from .splitter import split_document_by_structure
from .chunk_exporter import save_chunks_as_json
from .embedding import EmbeddingModel, embed_chunks
from .vector_store import VectorStore
from .retriever import Retriever
from .chunk_loader import load_chunks_from_json
from .llm_client import LLMClient
from .prompt import build_prompt
from .config import (
    OLLAMA_BASE_URL,
    LLM_MODEL,
)


def build_document(file_path: Path) -> Document:
    """读取、清洗并构造统一文档结构。"""

    raw_text = load_text(file_path)

    if file_path.suffix.lower() == ".pdf":
        cleaned_text = clean_pdf_text(
            raw_text
        )
    else:
        cleaned_text = clean_text(
            raw_text
        )

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

            chunks = split_document_by_structure(
                document,
                max_chunk_size=400,
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
    top_k: int = 5,
) -> str:
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

    search_results = retriever.search(
        query,
        top_k=top_k,
        debug=True
    )

    if not search_results:
        return "知识库中没有找到足够相关的信息。"

    chunks = [
        result.chunk
        for result in search_results
    ]

    prompt = build_prompt(
        query,
        chunks,
    )

    llm_client = LLMClient(
        base_url=OLLAMA_BASE_URL,
        model=LLM_MODEL,
    )
    answer = llm_client.generate(
    prompt
    )


    return answer

