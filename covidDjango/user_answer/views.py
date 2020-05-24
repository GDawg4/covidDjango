from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from user_answer.models import UserAnswer
from user_answer.serializers import UserAnswerSerializer

class UserAnswerViewSet(viewsets.ModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
