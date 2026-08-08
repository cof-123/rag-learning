from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


request = ChatRequest(
    question="What is RAG?"
)


print(request)

print(request.question)