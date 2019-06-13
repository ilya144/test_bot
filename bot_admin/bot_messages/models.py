from django.db import models


class Message(models.Model):
    text = models.TextField("Сообщение при старте")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
