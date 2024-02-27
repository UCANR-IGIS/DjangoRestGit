from django.contrib import admin
from .models import GeeksModel


class GeeksAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "ready"]
    list_editable = ["description", "ready"]


# Register your models here.
admin.site.register(GeeksModel, GeeksAdmin)
