from django.db import models

class UploadList(models.Model):
    filename = models.CharField(max_length=120)
    upload = models.FileField(upload_to='%Y/%m/%d/', max_length=100)
    #  url = models.CharField(max_length=120)
    ip_address = models.CharField(max_length=15)

    def __str__(self):
        return self.filename