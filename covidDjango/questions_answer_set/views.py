from rest_framework import viewsets
from rest_framework.decorators import action

from questions_answer_set.models import QuestionsAnswerSet
from questions_answer_set.serializers import QuestionAnswerSerializers

class QuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset = QuestionsAnswerSet.objects.all()
    serializer_class = QuestionAnswerSerializers
