import requests


url = "http://127.0.0.1:8000/chat"


data = {
    "question": "What is RAG?"
}


response = requests.post(
    url,
    json=data,
)


print(response.status_code)

print(response.json())