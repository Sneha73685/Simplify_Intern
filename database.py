from motor.motor_asyncio import AsyncIOMotorClient
import os

# Load MongoDB URI from environment variables
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Create an asynchronous MongoDB client
client = AsyncIOMotorClient(MONGO_URI)

# Select database and collection
db = client["rag_csv_analyzer"]
csv_collection = db["csv_files"]
