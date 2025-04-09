from django.urls import path
from apps.questions.views import (
    home_view,
    question_detail_view,
    ask_question_view,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("<int:pk>/", question_detail_view, name="question_detail"),
    path("ask/", ask_question_view, name="ask_question"),
]
