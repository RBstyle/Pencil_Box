from django.shortcuts import render
from django.http import HttpResponse
from download.models import UploadList

def index(request):
    return render(request, 'host/index.html')

def upload(request):
    if request.method == 'POST':
        file = request.FILES['file']
        form = UploadList(request.POST, request.FILES)
        form.save()
        return redirect('upllist/')
    return render(request, 'host/upload.html')