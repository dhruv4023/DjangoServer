
from django.contrib import admin
from django.urls import path
from myserver.controller import *
urlpatterns = [
    path('', index, name="home"),
    path('project/addproject/', addProject, name="addproject"),
    path('project/getproject/', getProject, name="getproject"),
    path('project/delproject/<str:id>/', delProject, name="delProject"),
    path('project/editproject/<str:id>/', editProject, name="editProject"),
    path('admin/', admin.site.urls),
]
