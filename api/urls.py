from django.urls import path, include

from . import views

app_name = 'api'
urlpatterns = [
    path('', views.send_message_to_telegram_bot,
         name='send_message_to_telegram_bot')
]
