from fastapi import APIRouter
from database import csv_collection

router = APIRouter()

@router.get("/files")
async def get_files():
    files = await csv_collection.find({}, {"_id": 0, "file_id": 1, "file_name": 1}).to_list(None)
    return {"files": files}
