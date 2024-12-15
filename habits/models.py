from django.db import models
from django.contrib.auth.models import User

from config import settings


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Поле для связи с пользователем, который создал привычку. При удалении пользователя, привычка также будет удалена.

    name = models.CharField(max_length=255)
    # Название привычки, строка длиной до 255 символов.

    place = models.CharField(max_length=255)
    # Место выполнения привычки, строка длиной до 255 символов.

    time = models.TimeField()
    # Время выполнения привычки.

    action = models.CharField(max_length=255)
    # Действие, которое выполняется в рамках привычки, строка длиной до 255 символов.

    is_pleasant = models.BooleanField(default=False)
    # Флаг, указывающий, является ли привычка приятной.

    related_habit = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                                      limit_choices_to={'is_pleasant': True})
    # Связь с другой привычкой, которая является приятной. Может быть пустым.

    reward = models.CharField(max_length=255, null=True, blank=True)
    # Награда за выполнение привычки, строка длиной до 255 символов. Может быть пустым.

    frequency = models.PositiveIntegerField(default=1)
    # Частота выполнения привычки, по умолчанию ежедневно (1 день).

    estimated_time = models.PositiveIntegerField(help_text="Время в секундах")
    # Оценочное время выполнения привычки в секундах.

    is_public = models.BooleanField(default=False)
    # Флаг, указывающий, является ли привычка публичной.

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.reward and self.related_habit:
            raise ValidationError("Cannot have both a reward and a related habit.")

        if self.estimated_time > 120:
            raise ValidationError("Estimated time must be 120 seconds or less.")

        if self.frequency > 7:
            raise ValidationError("Frequency must be at least once every 7 days.")

        if self.is_pleasant and (self.reward or self.related_habit):
            raise ValidationError("Pleasant habits cannot have rewards or related habits.")

    def __str__(self):
        return f"{self.action} at {self.time} in {self.place}"

