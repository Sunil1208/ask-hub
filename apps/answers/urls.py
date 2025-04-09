from django.urls import path
from apps.answers.views import AnswerListCreateView, LikeToggleView

urlpatterns = [
    path(
        "questions/<int:question_id>/",
        AnswerListCreateView.as_view(),
        name="answer_list_create",
    ),
    path("<int:answer_id>/like", LikeToggleView.as_view(), name="like_toggle"),
]
