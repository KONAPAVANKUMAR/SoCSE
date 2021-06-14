from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(AchievementModel)
class AchievementModelAdmin(admin.ModelAdmin):
    list_display = ("user","description","date")
