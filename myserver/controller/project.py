import json
import time
from django.http import *
from bson.objectid import *
from myserver.mongodb import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import *


@csrf_exempt
def getProject(request):
    cursor = project_collection.find()
    documents = list(cursor)
    return HttpResponse(json.dumps(documents), content_type='application/json')


@csrf_exempt
def addProject(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            doc = {
                "_id": str(int(round(time.time() * 10))),
                "title": data.get('title'),
                "link": data.get('link'),
                "description": data.get('description'),
            }
            project_collection.insert_one(doc)
            return HttpResponse(json.dumps({"msg": "JSON data Saved"}), content_type='application/json')
        except json.JSONDecodeError:
            return HttpResponse(json.dumps({"msg": "Invalid JSON data"}), content_type='application/json')
    else:
        return HttpResponse("Server Error")


@csrf_exempt
def delProject(request, id):
    print(id)
    try:
        if request.method == 'DELETE':
            project_collection.find_one_and_delete({"_id": id})
            return HttpResponse("Successfully deleted")
        else:
            return HttpResponseBadRequest("Request Not Allowed")
    except:
        return HttpResponseBadRequest("Invalid Project Id")


@csrf_exempt
def editProject(request, id):
    print(id, request.method)

    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            doc = {
                "title": data.get('title'),
                "link": data.get('link'),
                "description": data.get('description'),
            }
            find = {"_id": id}
            update = {"$set": doc}
            project_collection.find_one_and_update(find, update)
            return HttpResponse("Successfully Edited")
    except:
        return HttpResponseBadRequest("Invalid Project Id")
