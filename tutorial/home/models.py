from django.db import models

# Create your models here.
class fileupload(models.Model):
    img=models.FileField()