from django.shortcuts import get_object_or_404, redirect
from apps.answers.models import Answer, Like
from django.contrib.auth.decorators import login_required


@login_required
def like_toggle(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    like, created = Like.objects.get_or_create(user=request.user, answer=answer)

    if not created:
        like.delete()

    return redirect(request.META.get("HTTP_REFERER", "/"))
