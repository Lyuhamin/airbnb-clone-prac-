from django.contrib import admin
from .models import House

@admin.register(House)
class HouseAsmin(admin.ModelAdmin):
    pass
