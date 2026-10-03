from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import base64
import mimetypes
from fastapi.responses import FileResponse
from pydantic import BaseModel
#uvicorn main:app --reload
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_methods=["GET","POST"],
    allow_headers=["*"],
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
    path = f"{filename}"
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
    return {"received": user_text, "length": len(user_text)}