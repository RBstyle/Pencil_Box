from django.http import HttpResponseRedirect
from django.http import HttpResponse
from download.models import UploadList


def download(request):
    f = UploadList.objects.get(id=request.POST['file_id'])
    file = f.upload
    file_name = f.filename
    key_ip = f.ip_address
    ip = request.META['REMOTE_ADDR']
    if ip == key_ip:
        response = HttpResponse(file, content_type='multipart/form-data')
        response['Content-Disposition'] = 'attachment; filename=' + file_name
        return response
    return HttpResponseRedirect('/')


def link(request):
    return HttpResponseRedirect('/')
