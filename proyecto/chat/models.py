from django.db import models


class Conversation(models.Model):
    room_name = models.CharField(max_length=255, unique=True,verbose_name="room_name")
    user1 = models.CharField(max_length=255,verbose_name="user1")
    user2 = models.CharField(max_length=255,verbose_name="user2")
    class Meta:
        verbose_name_plural = "Conversaciones"
        verbose_name = "Conversacion"

    def __str__(self):
        return self.room_name
    
    
class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender =models.CharField(max_length=255,verbose_name="sender")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Mensajes"
        verbose_name = "Mensaje"
    def __str__(self):
        return f"{self.sender}: {self.content}"