from django.urls import path
from apps.questions.views import (
    QuestionListCreateView,
    # QuestionRetrieveView,
    # QuestionDeleteView,
    QuestionRetrieveOrDeleteView,
)

urlpatterns = [
    path("", QuestionListCreateView.as_view(), name="question_list_create"),
    path(
        "<int:pk>/",
        QuestionRetrieveOrDeleteView.as_view(),
        name="question_retrieve_or_delete",
    ),
]
