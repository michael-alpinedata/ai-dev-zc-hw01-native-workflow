from django.contrib import admin

from .models import Household, Member


@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("user", "household", "role", "joined_at")
    list_filter = ("role",)
    search_fields = ("user__username", "user__email", "household__name")
