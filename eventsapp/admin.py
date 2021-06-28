from django.contrib import admin
from django.utils.html import format_html
from .models import *
# Register your models here.
@admin.register(EventModel)
class EventModelAdmin(admin.ModelAdmin):
    list_display = ("name","type","datetime","organiser","print_data")
    def print_data(self, obj):
        return format_html('<a style="color:blue" href="/events/'+ str(obj.id) +'/print/">print</a>')
    print_data.allow_tags = True

@admin.register(EventTypeModel)
class EventTypeModelAdmin(admin.ModelAdmin):
    list_display = ("name",)



@admin.register(FeaturedModel)
class FeaturedModelAdmin(admin.ModelAdmin):
    list_display = ("event",)
