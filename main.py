from fastapi import FastAPI, UploadFile, File
import shutil

from gemini_parser import extract_questions_from_pdf

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MBBS PYQ Scanner Running"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    path = f"uploads/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    questions = extract_questions_from_pdf(path)

    return {
        "message": "PDF processed successfully",
        "questions": questions
    }