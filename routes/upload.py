from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
import uuid
from database import csv_collection

router = APIRouter()

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed.")

    df = pd.read_csv(file.file)
    file_id = str(uuid.uuid4())

    csv_data = df.to_dict(orient="records")  # Convert to JSON-like format

    await csv_collection.insert_one({
        "file_id": file_id,
        "file_name": file.filename,
        "document": csv_data
    })

    return {"file_id": file_id, "message": "Upload successful"}
