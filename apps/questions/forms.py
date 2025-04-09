from django import forms
from apps.questions.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title", "description"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }
