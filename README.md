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
```  
**Errors:**  
- `400 Bad Request`: Invalid file format  
- `500 Internal Server Error`: Storage issues  

### 2. Get Uploaded Files  
**Endpoint:** `GET /files`  
**Description:** Retrieves a list of uploaded CSV files.  
**Response:**  
```json  
{  
  "files": [  
    {  
      "file_id": "string",  
      "file_name": "string"  
    }  
  ]  
}  
```  
**Errors:**  
- `500 Internal Server Error`: Retrieval failure  

### 3. Query CSV Data  
**Endpoint:** `POST /query`  
**Description:** Queries a specific CSV file using an LLM.  
**Input:**  
```json  
{  
  "file_id": "string",  
  "query": "string"  
}  
```  
**Response:**  
```json  
{  
  "response": "string"  
}  
```  
**Errors:**  
- `404 Not Found`: File not found  
- `400 Bad Request`: Missing parameters  

### 4. Delete CSV File  
**Endpoint:** `DELETE /file/{file_id}`  
**Description:** Deletes a CSV file from the database.  
**Response:**  
```json  
{  
  "message": "File deleted successfully"  
}  
```  
**Errors:**  
- `404 Not Found`: File does not exist  
- `500 Internal Server Error`: Deletion failure  

## Setup & Installation  

### 1. Prerequisites  
Ensure you have the following installed:  
- Python 3.8+  
- MongoDB (local or cloud, e.g., MongoDB Atlas)  

### 2. Clone Repository  
```sh  
git clone <repository-url>  
cd rag-csv-analyzer  
```

### 3. Create a Virtual Environment  
```sh  
python -m venv venv  
source venv/bin/activate  # On Windows use `venv\Scripts\activate`  
```

### 4. Install Dependencies  
```sh  
pip install -r requirements.txt  
```

### 5. Set Up Environment Variables  
Create a `.env` file in the root directory and add:  
```env  
MONGO_URI=mongodb://localhost:27017  
OPENAI_API_KEY=your-api-key  
```

### 6. Run the Server  
```sh  
uvicorn main:app --host 0.0.0.0 --port 8000 --reload  
```

### 7. API Documentation  
Once the server is running, access API docs at:  
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- Redoc UI: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

## Deployment  
To deploy the application, you can use services such as:  
- **Docker**: Build and run using a Docker container.  
- **Heroku**: Deploy using Heroku for a cloud-hosted API.  
- **AWS/GCP**: Deploy on cloud platforms with serverless options.  

## Contribution  
Contributions are welcome. Please follow these steps:  
1. Fork the repository  
2. Create a feature branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m "Description of changes"`)  
4. Push to the branch (`git push origin feature-name`)  
5. Open a pull request  

## License  
This project is licensed under the MIT License.  
