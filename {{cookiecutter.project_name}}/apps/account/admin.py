from django.contrib import admin

from core.admin.base import BaseAdmin
from . import models


@admin.register(models.User)
class UserAdmin(BaseAdmin):
    list_display = ("id", "full_name", "email", "is_staff")
    search_fields = ("first_name", "last_name", "email")

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("role")

