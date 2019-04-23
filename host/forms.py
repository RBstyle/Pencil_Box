from django import forms
from django.forms import ModelForm
from download.models import UploadList


class UploadListForm(forms.ModelForm):
    class Meta:
        model = UploadList
        fields = ('upload', )
