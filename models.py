from pydantic import BaseModel
from typing import List, Optional

class CSVUploadRequest(BaseModel):
    file_path: str  # For fetching files from a directory

class CSVQueryRequest(BaseModel):
    file_id: str
    query: str

class CSVFileMetadata(BaseModel):
    file_id: str
    file_name: str
    document: List[List[str]]  # CSV stored as a list of rows
