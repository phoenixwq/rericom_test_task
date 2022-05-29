from abc import ABC

from rest_framework import serializers
from .models import Message
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class MessageSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=UserModel.objects.all(),
        source="user"
    )
    text = serializers.CharField()

    class Meta:
        model = Message
        fields = ('user_id', 'text')


class MessageConfirmSerializer(serializers.Serializer):
    message_id = serializers.PrimaryKeyRelatedField(
        queryset=Message.objects.all(),
        source="id"
    )
    success = serializers.BooleanField()
