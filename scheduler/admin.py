from django.contrib import admin
from scheduler.models import WowClass, WowRole, Character, WowSecondaryRole


@admin.register(WowClass)
class WowClassAdmin(admin.ModelAdmin):
    list_display = (
        "character_class",
    )

@admin.register(WowRole)
class WowRoleAdmin(admin.ModelAdmin):
    list_display = (
        "role",
    )

@admin.register(WowSecondaryRole)
class WowSecondaryRoleAdmin(admin.ModelAdmin):
    list_display = (
        "secondary_role",
    )

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "primary_role",
        "secondary_role",
        "character_class",
    )
