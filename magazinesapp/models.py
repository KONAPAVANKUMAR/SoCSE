from django.db import models

# Create your models here.
class MagazineModel(models.Model):
    name = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    pdf = models.FileField(upload_to='magazines/')
    date = models.DateField()