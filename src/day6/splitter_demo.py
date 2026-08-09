def split_text(
    text: str,
    chunk_size: int,
    overlap: int,
) -> list[str]:

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        if end >= len(text):
            break

        start = end - overlap

    return chunks





print("\n测试overlap\n")


text2 = "ABCDEFGHIJK"


chunks2 = split_text(
    text2,
    chunk_size=5,
    overlap=2,
)


for index, chunk in enumerate(chunks2):
    print(index, chunk)