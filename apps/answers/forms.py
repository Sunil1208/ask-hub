from django import forms
from apps.answers.models import Answer


class AnswerForm(forms.ModelForm):
    content = forms.CharField(
        label="Your answer",
        widget=forms.Textarea(
            attrs={"rows": 4, "placeholder": "Type your answer here..."}
        ),
    )

    class Meta:
        model = Answer
        fields = ("content",)
