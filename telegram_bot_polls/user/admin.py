from django.contrib import admin
from user.models import PollModel, UserProfileModel


@admin.register(UserProfileModel)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("telegram_chat_id", "completed_polls")
    search_fields = ("telegram_chat_id", "completed_polls")


@admin.register(PollModel)
class PollAdmin(admin.ModelAdmin):
    list_display = ("question", "user_profile", "poll_id", "created_at")
    search_fields = ("question", "user_profile", "poll_id")
    list_filter = ("created_at", )
    readonly_fields = ("created_at", "updated_at", "poll_id")
    fieldsets = (
        (None, {
            "fields": ("question", "user_profile", "options")
        }),
        (
            "Системные поля(не редактировать!)", {
                "fields": (
                    "user_options",
                    "poll_id",
                    "created_at",
                    "updated_at"
                ),
                "classes": ("collapse",)
            }
        )
    )
# Register your models here.
