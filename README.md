# RAG CSV Analyzer – FastAPI Backend  

## Overview  
This project is a FastAPI-based API that enables users to upload and query CSV files using Retrieval-Augmented Generation (RAG). It efficiently stores CSV data in MongoDB and allows users to interact with it via chat using an LLM.  

## Features  
- Accepts CSV files from various sources:  
  - Direct file upload  
  - Fetch from a predefined disk location  
  - Pick from a project directory  
- Extracts, indexes, and stores CSV content in MongoDB  
- Provides an API for querying and interacting with CSV data using an LLM  
- Supports OpenAI's GPT models or Hugging Face open-source LLMs  
- Implements proper error handling and status codes  

## Technology Stack  
- **Backend Framework**: FastAPI  
- **Database**: MongoDB (MySQL optional)  
- **LLM Integration**: OpenAI API or Hugging Face models  
- **Other Dependencies**: Pandas, Motor, Uvicorn, Transformers  

## API Endpoints  

### 1. Upload CSV  
**Endpoint:** `POST /upload`  
**Description:** Uploads a CSV file and stores it in the database.  
**Input:** Multipart form-data (CSV file) or JSON (file path)  
**Response:**  
```json
{
  "file_id": "string",
  "message": "Upload successful"
}
