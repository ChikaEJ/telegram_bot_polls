from django.urls import path
from telegram_bot_polls.bot import views

urlpatterns = [
    path('webhook', views.telegram_webhook, name='webhook'),
]
