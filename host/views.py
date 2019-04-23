from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from download.models import UploadList
from .forms import UploadListForm


def index(request):
    return render(request, 'host/index.html')


def upload(request):
    if request.method == 'POST':
        form = UploadListForm(request.POST, request.FILES)
        if form.is_valid():
            upl_file = form.save(commit=False)
            upl_file.filename = upl_file.upload.file.name
            upl_file.ip_address = request.META['REMOTE_ADDR']
            upl_file.save()
        return HttpResponseRedirect('/upllist/')
    else:
        form = UploadListForm()
    return render(request, 'host/upload.html', {
        'form': form
    })
