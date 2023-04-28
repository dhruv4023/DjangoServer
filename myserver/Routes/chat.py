
from django.urls import path
from myserver.controller.chat import *
urlpatterns = [
    path('getChatData/<str:id>', getChatData, name="getChatData"),
    path('addNewMsg/<str:id>', addNewMsg, name="addNewMsg"),
    path('delChat/<str:id>/', delChat, name="delChat"),
    path('chatuserlist/', chatLserList, name="chatuserlist"),
]
