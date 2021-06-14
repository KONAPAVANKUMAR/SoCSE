from django.db import models
from django.contrib.auth.models import User
# Create your models here.
def get_name(self):
    if self.username=="admin":
        return "admin"
    return self.first_name + " "+self.last_name
User.add_to_class("__str__", get_name)
