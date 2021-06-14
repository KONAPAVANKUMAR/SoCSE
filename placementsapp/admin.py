from django.contrib import admin
from .models import PlacementsModel,CompanyModel
# Register your models here.
@admin.register(PlacementsModel)
class PlacementsModelAdmin(admin.ModelAdmin):
    list_display = ("company_name","date")

@admin.register(CompanyModel)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ("name",)