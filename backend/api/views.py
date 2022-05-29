from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    MessageSerializer,
    MessageConfirmSerializer
)
from .producers import send


@api_view(["POST"])
def message(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        message = serializer.save()
        send(
            {
                "message_id": message.pk,
                "text": message.text
            }
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def message_confirmation(request):
    serializer = MessageConfirmSerializer(data=request.data)
    if serializer.is_valid():
        success = serializer.validated_data.get("success")
        message = serializer.validated_data.get("id")
        if success:
            message.status = "correct"
        else:
            message.status = "blocked"
        message.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
