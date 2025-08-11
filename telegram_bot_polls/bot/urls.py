from bot import views
from django.urls import path

urlpatterns = [
    path('webhook/', views.telegram_webhook, name='webhook'),
]
