from apps.questions.models import Question
from django.shortcuts import render, get_object_or_404, redirect
from apps.answers.forms import AnswerForm
from django.contrib import messages
from apps.questions.forms import QuestionForm

from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
    questions = Question.objects.all().order_by("-created_at")
    return render(request, "questions/home.html", {"questions": questions})


@login_required
def question_detail_view(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.select_related("user").order_by("-created_at")

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.save()
            messages.success(request, "Answer posted successfully!")
            return redirect("question_detail", pk=question.pk)
    else:
        form = AnswerForm()

    return render(
        request,
        "questions/question_detail.html",
        {"question": question, "answers": answers, "form": form},
    )


@login_required
def ask_question_view(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            messages.success(request, "Question posted successfully!")
            return redirect("home")
        else:
            messages.error(request, "Error posting question")
    else:
        form = QuestionForm()
    return render(request, "questions/aks_question.html", {"form": form})  # render
