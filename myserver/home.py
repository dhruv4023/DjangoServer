from django.shortcuts import render
from django.http import *
import json
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Server is running")


@csrf_exempt
def adminLogin(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            if data.get("code") == settings.CODE:
                print(data)
                return HttpResponse(json.dumps({"statusCode": True}), content_type='application/json')
            return HttpResponse(json.dumps({"statusCode": False}), content_type='application/json')
    except json.JSONDecodeError:
        return HttpResponse(json.dumps({"msg": "Invalid JSON data"}), content_type='application/json')

    except:
        return HttpResponse(json.dumps({"msg": "Server Error"}), content_type='application/json')
    return HttpResponse(json.dumps({"msg": "Server Error"}), content_type='application/json')
