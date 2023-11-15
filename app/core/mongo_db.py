from pymongo import MongoClient
from pymongo.database import Database

client: MongoClient = MongoClient("mongodb://mongodb/")
db: Database = client["mongodb"]
collection = db["collection"]
