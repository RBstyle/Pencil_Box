from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from download.models import UploadList


def get_file(request, id):
    if request.method == 'POST':
        f = UploadList.objects.get(id=request.POST['file_id'])
        file = f.upload
        file_name = f.filename
        response = HttpResponse(file, content_type='multipart/form-data')
        response['Content-Disposition'] = 'attachment; filename=' + file_name
        return response
    f = UploadList.objects.get(id=id)
    key_ip = f.ip_address
    ip = request.META['REMOTE_ADDR']
    access = False
    if ip == key_ip:
        access = True
    return render(request, 'download/get_file.html', {'id': id,
                                                      'access': access})
