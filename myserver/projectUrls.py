
from django.urls import path
from myserver.controller import *
urlpatterns = [
    path('addproject/', addProject, name="addproject"),
    path('getproject/', getProject, name="getproject"),
    path('delproject/<str:id>/', delProject, name="delProject"),
    path('editproject/<str:id>/', editProject, name="editProject"),
]
