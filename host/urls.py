from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('upllist/', include('download.urls')),
    path('upload/', views.upload, name='upload')
]
