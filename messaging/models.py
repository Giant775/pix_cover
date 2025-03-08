from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from users.models import Users

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='message_sender')
    receiver = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='message_receiver')
    content = models.TextField()
    file = models.FileField(upload_to=None, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender.fullname} to {self.receiver.fullname}'