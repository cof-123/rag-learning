import requests


class LLMClient:
    def __init__(
        self,
        base_url: str,
        model: str,
    ) -> None:
        self.base_url = base_url
        self.model = model

    def generate(
        self,
        prompt: str,
    ) -> str:
        url = (
            f"{self.base_url}"
            "/v1/chat/completions"
        )

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            "temperature": 0,
        }

        response = requests.post(
            url,
            json=payload,
            timeout=300,
        )

        response.raise_for_status()

        data = response.json()

        return data[
            "choices"
        ][0][
            "message"
        ][
            "content"
        ]