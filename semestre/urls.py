from django.contrib import admin
from django.urls import path
from .views import listagem_semestre


urlpatterns = [
    path('listagem/', listagem_semestre),
]
