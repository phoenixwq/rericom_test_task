from django.urls import path
from .views import message, message_confirmation

urlpatterns = [
    path('v1/message/', message),
    path("v1/message_confirmation/", message_confirmation)
]
