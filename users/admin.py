from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile", 
            {
                "fields": (
                    "avatar",
                    "username", 
                    "password", 
                    "name", 
                    "email", 
                    "is_host",
                    "gender",
                    "curreny",
                    "language",
                ),
                "classes": ("wide",),
            },
        ),

        ("Permissions", 
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),

        (
            "important Dates", 
            {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",),
            },
        ),

    )

    list_display = ("username", "email", "name", "is_host")