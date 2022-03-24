from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Semestre


# Create your views here.
def listagem_semestre(request):
    semestre = Semestre.objects.all().first()
    return HttpResponse(f'Codigo: {semestre.codigo} - Descricao {semestre.descricao}')
