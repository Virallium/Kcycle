from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notification(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification {self.id} - {self.message[:50]}"

class Reception(models.Model):
    Date_reception = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptions')
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name='receptions')

    def __str__(self):
        return f"Message reçu {self.id} - {self.Date_reception}"
