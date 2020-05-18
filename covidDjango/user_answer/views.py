from rest_framework import viewsets

from user_answer.models import UserAnswer
from user_answer.serializers import UserAnswerSerializer

class UserAnswerViewSet(viewsets.ModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer