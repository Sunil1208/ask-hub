from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.answers.models import Answer, Like
from apps.questions.models import Question
from apps.answers.serializers import AnswerSerializer, LikeSerializer


class AnswerListCreateView(APIView):
    """
    GET => /answers/questions/<question_id>/ - Lists all answers for a given question
    POST => /answers/questions/<question_id>/ - Creates a new answer for a given question
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, question_id):
        answers = Answer.objects.filter(question_id=question_id).order_by("-created_at")
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

    def post(self, request, question_id):
        # validate the existence of questions
        try:
            question = Question.objects.get(id=question_id)
        except question.DoesNotExist:
            return Response(
                {"detail": "Question not found"}, status=status.HTTP_404_NOT_FOUND
            )

        data = (
            request.data.copy()
        )  # Make a mutable copy, in case if data updation is required in feature

        serializer = AnswerSerializer(data=data)

        if serializer.is_valid():
            # Attach user and question
            serializer.save(user=request.user, question=question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeToggleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, answer_id):
        try:
            answer = Answer.objects.get(id=answer_id)
        except Answer.DoesNotExist:
            return Response(
                {"detail": "Answer not found"}, status=status.HTTP_404_NOT_FOUND
            )

        like, created = Like.objects.get_or_create(answer=answer, user=request.user)

        if not created:
            # Already liked, remove it to unlike
            like.delete()
            return Response({"detail": "Unlike"}, status=status.HTTP_200_OK)
        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
