from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "API server running"
    }


@app.post("/chat")
def chat(data: dict):

    question = data["question"]

    return {
        "answer": f"You asked: {question}"
    }