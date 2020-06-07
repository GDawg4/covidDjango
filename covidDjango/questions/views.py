from rest_framework import viewsets

from questions.models import Questions
from questions.serializers import QuestionsSerializer

class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

