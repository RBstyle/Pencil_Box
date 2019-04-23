from django.urls import path, include
from django.views.generic import ListView, DetailView
from download.models import UploadList
from . import views

urlpatterns = [
    path(
         '',
         ListView.as_view(
                          queryset=UploadList.objects.all().order_by('filename'),
                          template_name='download/filelist.html'
                         )
         ),
    path('download/', views.download),
]
