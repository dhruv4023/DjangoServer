import json
import time
from django.http import *
from bson.objectid import *
from myserver.mongodb import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import *



@csrf_exempt
def getContact(request):
    cursor = contact_collection.find()
    documents = list(cursor)
    return HttpResponse(json.dumps(documents), content_type='application/json')


@csrf_exempt
def addContact(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            doc = {
                "_id": str(int(round(time.time() * 10))),
                "name": data.get('name'),
                "email": data.get('email'),
                "msg": data.get('msg'),
            }
            contact_collection.insert_one(doc)
            return HttpResponse("JSON data Saved")
            # return HttpResponse(json.dumps(np), content_type='application/json')
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON data")
    else:
        return HttpResponse("Server Error")


@csrf_exempt
def delContact(request, id):
    try:
        if request.method == 'DELETE':
            contact_collection.find_one_and_delete({"_id": id})
            return HttpResponse("Successfully deleted")
        else:
            return HttpResponseBadRequest("Request Not Allowed")
    except:
        return HttpResponseBadRequest("Invalid contact Id")
