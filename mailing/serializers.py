from rest_framework import serializers

from .models import Recipient, Result, Message, Mailing


class MailingSerializer(serializers.ModelSerializer):
    """ML serializer"""
    class Meta:
        model = Mailing
        fields = ['__all__']


class MessageSerializer(serializers.ModelSerializer):
    """Message serializer"""

    class Meta:
        model = Message
        fields = ['__all__']


class ResultSerializer(serializers.ModelSerializer):
    """Mailing serializer"""

    class Meta:
        model = Result
        fields = ['__all__']
