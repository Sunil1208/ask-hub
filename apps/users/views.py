from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from apps.users.forms import CustomUserCreationForm, CustomLoginForm

from django.contrib.auth import get_user_model


User = get_user_model()


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful")
            return redirect("login")
        else:
            print("Form errors: ", form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful")
            return redirect("home")
    else:
        form = CustomLoginForm()
    return render(request, "users/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("login")


@login_required
def profile_view(request):
    user = request.user
    questions = user.questions.all().order_by("-created_at")
    answers = user.answers.all().select_related("question").order_by("-created_at")

    return render(
        request,
        "users/profile.html",
        {
            "user_obj": user,
            "questions": questions,
            "answers": answers,
        },
    )
