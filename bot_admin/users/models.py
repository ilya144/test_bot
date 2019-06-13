from django.db import models


class User(models.Model):
    tg_id = models.IntegerField(unique=True, blank=False, verbose_name="ID")
    username = models.CharField(max_length=60, blank=True, unique=True, verbose_name="@username")
    first_name = models.CharField(max_length=60, blank=False, unique=True, verbose_name="Имя")
    last_name = models.CharField(max_length=60, blank=True, null=True, unique=True, verbose_name="Фамилия")

    def __str__(self):
        if self.username:
            return f"@{self.username}"
        else:
            return f"Пользователь ID={self.tg_id}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
