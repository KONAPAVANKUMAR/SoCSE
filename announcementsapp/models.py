from django.db import models

# Create your models here.
class AnnouncementsModel(models.Model):
    description = models.TextField()
    def __str__(self):
        return self.description