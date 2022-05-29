from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Message(models.Model):
    STATUSES = (
        ("review", "review"),
        ("blocked", "blocked"),
        ("correct", "correct")
    )
    status = models.CharField(
        choices=STATUSES,
        max_length=8,
        default="review"
    )
    text = models.TextField()
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="messages"
    )
    