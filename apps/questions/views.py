from rest_framework import generics, permissions
from apps.questions.models import Question
from apps.questions.serializers import QuestionSerializer
from rest_framework import status


class QuestionListCreateView(generics.ListCreateAPIView):
    """
    GET -> /questions/ - List all questions
    POST -> /questions/ - Create a new question (requires auth)
    """

    queryset = Question.objects.all().order_by("-created_at")
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Sets the user to the currently logged-in user
        serializer.save(user=self.request.user)


class QuestionRetrieveOrDeleteView(generics.RetrieveDestroyAPIView):
    """
    GET -> /questions/{id}/ - Retrieve a question
    DELETE -> /questions/{id}/ - Delete a question (requires auth)
    """

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # For the delete, we need to verify if the user deleting the question,
    # is the same user who created it
    def delete(self, request, *args, **kwargs):
        question = self.get_object()
        if question.user != request.user:
            return Response(
                {"error": "You can't delete a question that's not yours"},
                status=status.HTTP_403_FORBIDDEN,
            )
        # If the user is the same, we can delete the question
        return super().delete(request, *args, **kwargs)
