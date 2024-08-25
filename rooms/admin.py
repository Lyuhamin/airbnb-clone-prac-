from django.contrib import admin
from .models import Room, Amenity 

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    
    list_display = (
        "neme",
        "price",
        "kind",
        "owner",
    )

    list_filter = (
        "country",
        "city",
        "price",
        "toilets",
        "pet_friendly",
        "kind",
        "amenities",
    )

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    
    list_display = (
        "neme",
        "description",
        "create_at",
        "update_at",
    )
    
    readonly_fields = (
        "create_at",
        "update_at",
    )
