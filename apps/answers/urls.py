from django.urls import path
from apps.answers.views import like_toggle


urlpatterns = [
    path("<int:answer_id>/like", like_toggle, name="like_toggle"),
]
