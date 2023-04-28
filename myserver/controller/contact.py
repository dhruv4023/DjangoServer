import json
import time
from datetime import datetime
from django.http import *
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
                "messagedOn": str(datetime.today())
            }
            contact_collection.insert_one(doc)
            return HttpResponse(json.dumps({"msg": "Form Submitted Successfully"}), content_type='application/json')

        except json.JSONDecodeError:
            return HttpResponseBadRequest(json.dumps({"msg": "Invalid JSON data"}), content_type='application/json')
        except:
            return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')
    else:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')


@csrf_exempt
def delContact(request, id):
    try:
        if request.method == 'DELETE':
            contact_collection.find_one_and_delete({"_id": id})
            return HttpResponse(json.dumps({"msg": "Successfully deleted"}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "Request Not Allowed"}), content_type='application/json')
    except:
        return HttpResponseBadRequest(json.dumps({"msg": "Invalid contact Id"}), content_type='application/json')
