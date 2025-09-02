from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi import Request
from pydantic import BaseModel

import server_data_functions as sdf
from client import game_running


class WordData(BaseModel):
    word: str

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/api/health")
async def health():
    return {"status": "ok"}

@app.get("/api/reset")
async def reset():
    sdf.initialize()
    return {"status": "ok"}

@app.options("/api/submit", status_code=200)
async def submit_options():
    return {"message": "OK"}


@app.post("/api/submit", status_code=200)
async def submit_word(data: WordData):
    print(f"Received word: {data.word}")
    sdf.process_word(data.word)
    print(sdf.last_syllable)
    if sdf.reject_input:
        return {"status": "rejected", "newWord": "", "gameOver": False}
    return {"status": "accepted", "newWord": "새벽녘", "gameOver": not sdf.game_running}
    # {"status": "rejected", ...}
    # {"status": "accepted", "newWord": "새벽녘", "gameOver": true}