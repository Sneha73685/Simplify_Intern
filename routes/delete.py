from fastapi import APIRouter, HTTPException
from database import csv_collection

router = APIRouter()

@router.delete("/file/{file_id}")
async def delete_file(file_id: str):
    result = await csv_collection.delete_one({"file_id": file_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="File not found.")

    return {"message": "File deleted successfully"}
