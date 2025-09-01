from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from pydantic import BaseModel

class WordData(BaseModel):
    word: str

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/api/health")
async def health():
    return {"status": "ok"}

@app.options("/api/submit", status_code=200)
async def submit_options():
    return {"message": "OK"}


@app.post("/api/submit", status_code=200)
async def submit_word(data: WordData):
    print(f"Received word: {data.word}")
    return {"message": "Word received", "word": data.word}
