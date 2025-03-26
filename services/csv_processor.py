import pandas as pd
import uuid
from database import csv_collection
from fastapi import HTTPException

async def process_csv(file):
    """
    Reads the uploaded CSV file, converts it into a structured format, and stores it in MongoDB.
    """
    try:
        df = pd.read_csv(file.file)
        file_id = str(uuid.uuid4())

        csv_data = df.to_dict(orient="records")  # Convert CSV to JSON-like format

        # Store in MongoDB
        await csv_collection.insert_one({
            "file_id": file_id,
            "file_name": file.filename,
            "document": csv_data
        })

        return {"file_id": file_id, "message": "Upload successful"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing CSV: {str(e)}")
