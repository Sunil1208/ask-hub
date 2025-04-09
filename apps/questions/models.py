from django.db import models
from django.contrib.auth import get_user_model
from apps.common.models import TimeStampedModel

User = get_user_model()


class Question(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    title = models.CharField(max_length=512)
    description = models.TextField()

    def __str__(self):
        return self.title
