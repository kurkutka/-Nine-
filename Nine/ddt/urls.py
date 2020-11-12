from django.urls import path
from . import views

'''Ссылки внутри приложения. Нас отсылает с views.py проекта по любой ссылке сюда, т.к. там указан шаблон ''. Тут идёт 
обработка всех урлов /wtf, /, /logout и т.д. и т.п. '''
urlpatterns = [
    path('register', views.register),
]