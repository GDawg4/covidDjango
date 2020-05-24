from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from users.models import Users
from user_answer.models import UserAnswer
from users.serializers import UsersSerializers
from answers.serializers import AnswerSerializers
from user_answer.serializers import UserAnswerSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset =  Users.objects.all()
    serializer_class = UsersSerializers

    @action(detail=True, url_path='phone', methods=['get'])
    def get_phone(self, request, pk=None):
        total = 0
        user = self.get_object()
        answers = UserAnswer.objects.all().filter(Q(id_user = user), Q(id_questions = 10))
        print(answers)
        serialized = UserAnswerSerializer(answers)
        return Response(serialized.data)
