from django.db import models
from apps.common.models import TimeStampedModel
from apps.questions.models import Question
from django.contrib.auth import get_user_model

User = get_user_model()


class Answer(TimeStampedModel):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="answers",
    )
    content = models.TextField()

    def __str__(self):
        return f"Answer by {self.user} on {self.question.title}"


class Like(TimeStampedModel):
    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
        related_name="likes",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="answer_likes",
    )

    class Meta:
        unique_together = ("answer", "user")

    def __str__(self):
        return f"{self.user} liked answer #{self.answer.id}"
