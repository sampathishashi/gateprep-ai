import os

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

client = MongoClient(MONGO_URI)

db = client[DATABASE_NAME]

users_collection = db["users"]
subjects_collection = db["subjects"]
pyqs_collection = db["pyqs"]
quiz_collection = db["quizzes"]
progress_collection = db["progress"]