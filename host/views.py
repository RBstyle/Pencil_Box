from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'host/index.html')

def upload(request):
    return render(request, 'host/upload.html')