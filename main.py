from fastapi import FastAPI
from routes import upload, files, query, delete

app = FastAPI(title="RAG CSV Analyser")

app.include_router(upload.router, prefix="/api")
app.include_router(files.router, prefix="/api")
app.include_router(query.router, prefix="/api")
app.include_router(delete.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to RAG CSV Analyser!"}
