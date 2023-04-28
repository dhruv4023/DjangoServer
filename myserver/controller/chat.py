import json
import time
from django.http import *
from myserver.mongodb import chat_collection
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import *
from datetime import datetime


@csrf_exempt
def getChatData(request, id):
    try:
        cursor = chat_collection.find_one({"_id": id})
        documents = dict(cursor)["msgs"]
        return HttpResponse(json.dumps(documents), content_type='application/json')
    except:
        return HttpResponseBadRequest(json.dumps({"msg": "No Chat Found"}), content_type='application/json')


@csrf_exempt
def addNewMsg(request, id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            doc = {
                "_id": str(int(round(time.time() * 10))),
                "side": data.get('side'),
                "message": data.get('message'),
                "messaged_on": str(datetime.today()),
            }
            chat_collection.find_one_and_update(
                {"_id": id}, {"$push": {"msgs": doc}})

            return HttpResponse(json.dumps({"msg": "JSON data Saved"}), content_type='application/json')

        except json.JSONDecodeError:
            return HttpResponse(json.dumps({"msg": "Invalid JSON data"}), content_type='application/json')

    else:
        return HttpResponse("Server Error")


@csrf_exempt
def delChat(request, id):
    try:
        if request.method == 'DELETE':
            chat_collection.find_one_and_delete({"_id": id})
            return HttpResponse(json.dumps({"msg": "Successfully deleted"}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "Request Not Allowed"}), content_type='application/json')
    except:
        return HttpResponseBadRequest(json.dumps({"msg": "Invalid contact Id"}), content_type='application/json')


def add_chat_to(name, email):
    data = chat_collection.find_one({"email": email})
    if data is None:
        id=str(int(round(time.time() * 10)))
        doc = {
            "_id": id,
            "name": name,
            "email": email,
            "msgs": [],
            "createdOn": str(datetime.today())
        }
        chat_collection.insert_one(doc)
        return id
    else:
        return data.get("_id")
