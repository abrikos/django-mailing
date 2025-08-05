from rest_framework import serializers

from .models import MailingList, Message, Sending


class MailingListSerializer(serializers.ModelSerializer):
    """ML serializer"""
    class Meta:
        model = MailingList
        fields = ['__all__']


class MessageSerializer(serializers.ModelSerializer):
    """Message serializer"""

    class Meta:
        model = Message
        fields = ['__all__']


class SendingSerializer(serializers.ModelSerializer):
    """Sending serializer"""

    class Meta:
        model = Sending
        fields = ['__all__']
