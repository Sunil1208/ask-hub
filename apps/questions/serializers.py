from rest_framework import serializers

from apps.questions.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    # better to show username instead of user ID here
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Question
        fields = ["id", "user", "title", "description", "created_at", "updated_at"]
