from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    CREATED = "Created"
    IN_PROGRESS = "In progress"
    DONE = "Done"

    STATUS_NOTE_CHOICES = [
        ("CR", CREATED),
        ("IP", IN_PROGRESS),
        ("DN", DONE)
    ]
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    status = models.CharField(choices=STATUS_NOTE_CHOICES, default=CREATED, max_length=11, verbose_name="Статус")
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь")

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"
        ordering = ["title", "status"]

    def __str__(self):
        return self.title
