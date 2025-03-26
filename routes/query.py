from fastapi import APIRouter, HTTPException
from database import csv_collection
from services.llm_handler import query_llm
from models import CSVQueryRequest

router = APIRouter()

@router.post("/query")
async def query_csv(request: CSVQueryRequest):
    csv_entry = await csv_collection.find_one({"file_id": request.file_id}, {"_id": 0})
    if not csv_entry:
        raise HTTPException(status_code=404, detail="File not found.")

    csv_data = csv_entry["document"]
    response = query_llm(request.query, csv_data)
    
    return {"response": response}
