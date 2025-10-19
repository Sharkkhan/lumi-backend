from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import requests, os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Lumi Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.get("/health")
def health():
    return {"ok": True, "message": "Lumi backend running"}

@app.post("/api/analyze/voice")
async def analyze_voice(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    files = {"file": (file.filename, audio_bytes, file.content_type)}
    data = {"model": "whisper-1", "response_format": "text"}
    r = requests.post(
        "https://api.openai.com/v1/audio/transcriptions",
        headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
        files=files,
        data=data
    )
    return {"transcript": r.text}

“Fix /health endpoint”
