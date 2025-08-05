from rest_framework import serializers

from .models import Recipient, Result, Message, Sending


class SendingSerializer(serializers.ModelSerializer):
    """ML serializer"""
    class Meta:
        model = Sending
        fields = ['__all__']


class MessageSerializer(serializers.ModelSerializer):
    """Message serializer"""

    class Meta:
        model = Message
        fields = ['__all__']


class ResultSerializer(serializers.ModelSerializer):
    """Sending serializer"""

    class Meta:
        model = Result
        fields = ['__all__']
