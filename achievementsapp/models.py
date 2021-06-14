from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AchievementModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=128)
    date = models.DateField()
    proof = models.FileField(upload_to='achievements/')
    approved = models.BooleanField(default=False)
