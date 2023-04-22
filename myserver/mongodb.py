from pymongo import MongoClient

from django.conf import settings

client = MongoClient(settings.DB_URL)
db = client["pymongotest"]
project_collection = db["projects"]
contact_collection = db["contacts"]
chat_collection = db["chat"]
messages_collection = db["messages"]
