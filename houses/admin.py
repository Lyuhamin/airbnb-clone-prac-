from django.contrib import admin
from .models import House


@admin.register(House)
class HouseAsmin(admin.ModelAdmin):

    list_display = (
        "name",
        "price_per_night",
        "address",
        "pets_allowed",
    )

    list_filter = (
        "price_per_night",
        "pets_allowed",
    )

    search_fields = [
        "adress_startswith"
    ]

    list_display_links = ("name", "address")
