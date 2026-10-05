from rest_framework import serializers

from .models import Conversation, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'conversation', 'content', 'sender', 'created_at')
        read_only_fields = ('id', 'conversation', 'sender', 'created_at')


class ConversationSerializer(serializers.ModelSerializer):
    dernier_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ('id', 'created_at', 'dernier_message')
        read_only_fields = fields

    def get_dernier_message(self, conversation):
        message = conversation.dernier_message()
        if message is None:
            return None
        return MessageSerializer(message, context=self.context).data