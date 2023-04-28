
from django.urls import path
from myserver.Mail.mail import *
urlpatterns = [
    path('sendotp/', sentOtp, name="sentOtp"),
    path('verifyOtp/', verifyOtp, name="verifyOtp"),
    # path('getcontact/', getContact, name="getcontact"),
    # path('delcontact/<str:id>/', delContact, name="delcontact"),
]

