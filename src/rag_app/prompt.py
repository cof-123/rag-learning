from .models import Chunk


def build_prompt(
    question: str,
    chunks: list[Chunk],
) -> str:
    """
    根据问题和检索结果构造Prompt。
    """

    context = "\n\n".join(
        chunk.content
        for chunk in chunks
    )

    prompt = f"""
你是一个企业知识库助手。

请根据下面提供的资料回答问题。

资料:
----------------
{context}
----------------

问题:
{question}

要求:
1. 只根据资料回答。
2. 如果资料中没有答案，请明确说明不知道。
"""

    return prompt.strip()