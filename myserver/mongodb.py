from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["pymongotest"]
project_collection = db["projects"]
contact_collection = db["contacts"]
chat_collection = db["chat"]
messages_collection = db["messages"]
