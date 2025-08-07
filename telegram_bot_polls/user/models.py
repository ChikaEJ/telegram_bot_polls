from django.db import models


class UserProfileModel(models.Model):
    telegram_chat_id = models.BigIntegerField(unique=True)
    completed_polls = models.PositiveIntegerField(default=0)

class PollModel(models.Model):
    user_profile = models.ForeignKey(
        to='user.UserProfileModel',
        on_delete=models.CASCADE,
        related_name='user_polls',
        db_index=True,
    )
    poll_id = models.BigIntegerField(null=True, blank=True)
    question = models.TextField()
    options = models.JSONField(default=list, null=True, blank=True)
    user_options = models.JSONField(default=list, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
