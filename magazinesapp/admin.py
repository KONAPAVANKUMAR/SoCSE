from django.contrib import admin
from .models import MagazineModel
# Register your models here.
@admin.register(MagazineModel)
class MagazineModelAdmin(admin.ModelAdmin):
    list_display = ("name","author","date")
