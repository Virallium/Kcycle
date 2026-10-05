from django.db import models
from django.contrib.auth.models import User


class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def dernier_message(self):
        return self.messages.last()
    
    def __str__(self):
        return f"Conversation {self.id} - User: {self.user}"


class Message(models.Model):
    SENDER_CHOICES = (
        ('user', 'Utilisateur'),
        ('bot', 'Assistant'),
    )

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    sender = models.CharField(max_length=4, choices=SENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at', 'id')
        indexes = [models.Index(fields=['conversation', 'created_at'])]
    
    def __str__(self):
        return f"Message {self.id} - Sender: {self.sender}"


