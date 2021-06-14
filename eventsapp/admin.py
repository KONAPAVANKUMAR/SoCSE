from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(EventModel)
class EventModelAdmin(admin.ModelAdmin):
    list_display = ("name","type","datetime","organiser")

@admin.register(EventTypeModel)
class EventTypeModelAdmin(admin.ModelAdmin):
    list_display = ("name",)



@admin.register(FeaturedModel)
class FeaturedModelAdmin(admin.ModelAdmin):
    list_display = ("event",)
