from rest_framework import serializers
from .models import Notification, Reception

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'message', 'created_at')
        read_only_fields = fields


class ReceptionSerializer(serializers.ModelSerializer):
    notification_message = serializers.CharField(
        source='notification.message',
        read_only=True,
    )

    class Meta:
        model = Reception
        fields = ('id', 'notification', 'notification_message', 'Date_reception', 'is_read')
        read_only_fields = ('id', 'notification_message', 'Date_reception', 'is_read')