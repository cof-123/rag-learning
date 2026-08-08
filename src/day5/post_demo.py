import requests


url = "https://httpbin.org/post"


data = {
    "question": "What is RAG?"
}


response = requests.post(
    url,
    json=data,
)


print("状态码:", response.status_code)


if response.status_code == 200:
    print(response.json())

else:
    print("请求失败")
    print(response.text)