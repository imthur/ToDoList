from django.urls import path
from .views import *

urlpatterns = [
    path('', todo_frontend),
    path('api/<int:pk>/', DetailToDo.as_view()),
    path('api/', ListToDo.as_view()),
    path('api/create', CreateToDo.as_view()),
    path('api/delete/<int:pk>', DeleteToDo.as_view()),
]