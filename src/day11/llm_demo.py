import requests


url = (
    "http://192.168.153.223:11434"
    "/v1/chat/completions"
)


payload = {
    "model": "deepseek-r1:32b",
    "messages": [
        {
            "role": "user",
            "content": "你好，请介绍一下RAG"
        }
    ],
    "temperature": 0.7,
}


response = requests.post(
    url,
    json=payload,
)


print(response.status_code)

data = response.json()

print(
    data
)