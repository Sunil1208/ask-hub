from rest_framework import serializers
from apps.answers.models import Answer, Like


class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    question = serializers.PrimaryKeyRelatedField(read_only=True)

    # we also need the number of likes
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = [
            "id",
            "user",
            "question",
            "content",
            "likes_count",
            "created_at",
            "updated_at",
        ]

    def get_likes_count(self, obj):
        return obj.likes.count()


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    answer = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = ["id", "user", "answer", "created_at", "updated_at"]
