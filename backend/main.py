from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import base64
import mimetypes
from fastapi.responses import FileResponse
import subprocess
import sys
from pathlib import Path

#uvicorn main:app --reload
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET","POST"],
    allow_headers=["*"],
    allow_credentials=False
)
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]
@app.get("/")
def read_root():
    return {"message": "FastAPI backend is running"}


@app.get("/video/{filename}")
async def get_video(filename: str):
    # Adjust path to your video folder
    path = f"C:/Users/juliu/Desktop/manim/backend/video/{filename}/images/derivatives_simple/Derivatives_ManimCE_v0.21.0.png"
    
    mime_type, _ = mimetypes.guess_type(path)
    return FileResponse(
        path,
        media_type=mime_type or "video/mp4",
        headers={"Accept-Ranges": "bytes"},
    )



@app.post("/send-text")
async def receive_text(data: dict):
    
    user_text = data.get("text")
    print(user_text)
    render_picture(user_text)
    return {"received": user_text, "length": len(user_text)}


def render_picture(text):
    subprocess.run(
        [
            sys.executable,
            "-m",
            "manim",
           "--media_dir","./video/"+str(text) ,
            "-qh",
            str("derivatives_simple.py"),
            "Derivatives",
        ],
        input=f"{text}\n",
        text=True,
        check=True,
    )