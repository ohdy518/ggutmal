from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi import Request
from pydantic import BaseModel

import server_data_functions as sdf
import server_auxiliary_functions as saf

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
    global user_wins
    user_wins = False
    sdf.initialize()
    return {"status": "ok"}

@app.options("/api/submit", status_code=200)
async def submit_options():
    return {"message": "OK"}

@app.post("/api/submit", status_code=200)
async def submit_word(data: WordData):
    if not sdf.game_running:
        return {"status": "rejected", "newWord": "", "definition": "", "gameOver": True, "userWins": sdf.user_wins}
    print(f"Received word: {data.word}")
    # TODO: deal this with SDF
    # if sdf.word_is_valid(data.word) and sdf.is_dead_end(data.word):
    #     user_wins = True
    #     return {"status": "accepted", "newWord": "", "definition": "", "gameOver": True, "userWins": user_wins}
    sdf.process_word(data.word)
    # print(sdf.last_syllable)
    if sdf.reject_input:
        return {"status": "rejected", "newWord": "", "gameOver": False}
    return {"status": "accepted", "newWord": sdf.agent_word, "definition": saf.define(sdf.agent_word), "gameOver": not sdf.game_running, "userWins": sdf.user_wins}
    # {"status": "rejected", ...}
    # {"status": "accepted", "newWord": "새벽녘", "gameOver": true}

@app.post("/api/define", status_code=200)
async def get_definition(data: WordData):
    return {"definition": saf.define(data.word)}
