import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from dserver.settings import EMAIL_HOST_USER
import random
from myserver.controller.chat import add_chat_to
MAIL_OTP = {}


@csrf_exempt
def sentOtp(request):
    if request.method == 'POST':
        try:
            to_mail = json.loads(request.body).get('email')
            otp = str(random.randint(100000, 999999))
            MAIL_OTP[to_mail] = otp
            # print(MAIL_OTP)
            # send_mail("TestMail", "Test Mail q", EMAIL_HOST_USER,
            #           [to_mail], fail_silently=True)
            return HttpResponse(json.dumps({"msg": "mail sent "+otp}), content_type='application/json')
        except json.JSONDecodeError:
            return HttpResponse(json.dumps({"msg": "Invalid JSON data"}), content_type='application/json')

    else:
        return HttpResponse("Server Error")


@csrf_exempt
def verifyOtp(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            name = body.get('name')
            email = body.get('email')
            otp = body.get('otp')
            if MAIL_OTP[email] == otp:
                add_chat_to(name, email)
                MAIL_OTP.pop(email)
                return HttpResponse(json.dumps({"msg": "Verified", "chat": True}), content_type='application/json')
            else:
                MAIL_OTP.pop(email)
                return HttpResponse(json.dumps({"msg": "Wrong OTP", "chat": False}), content_type='application/json')
        except json.JSONDecodeError:
            return HttpResponse(json.dumps({"msg": "Invalid JSON data"}), content_type='application/json')
        except:
            return HttpResponse(json.dumps({"msg": "resend OTP and try again"}), content_type='application/json')

    else:
        return HttpResponse("Server Error")
