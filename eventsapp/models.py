from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EventTypeModel(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name
class EventModel(models.Model):
    name = models.CharField(max_length = 128)
    type = models.ForeignKey(EventTypeModel,blank=True,null=True,on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=None,blank=True,null=True)
    organiser = models.CharField(max_length = 128,default=None,blank=True,null=True)
    description = models.TextField()
    participants = models.JSONField(blank = True,null = True,default = list)
    cover = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
    def get_year(self):
        return str(self.datetime.date().year)

class FeaturedModel(models.Model):
    event = models.ForeignKey(EventModel,on_delete=models.CASCADE)

