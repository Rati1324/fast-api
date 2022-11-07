from django.shortcuts import render
from .models import ToDo

def index(request):
    todos = ToDo.objects.all()
    return render(request, "index.html", {'todos': todos})