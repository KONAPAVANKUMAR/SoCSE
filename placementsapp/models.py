from django.db import models
from django.db.models.fields import DateField
from django.contrib.auth.models import User
# Create your models here.
class CompanyModel(models.Model):
    name = models.CharField(max_length=128)
    company_logo = models.ImageField(upload_to = 'company_logos/',blank = True,null = True,default = None)
    def __str__(self):
        return self.name
class PlacementsModel(models.Model):
    company_name = models.ForeignKey(CompanyModel,on_delete=models.CASCADE,blank=True,null=True)
    date = models.DateField()
    students = models.JSONField(default = list)

    def get_year(self):
        return str(self.date.year)
    