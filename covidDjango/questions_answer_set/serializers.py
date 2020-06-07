from rest_framework import serializers

from questions_answer_set.models import QuestionsAnswerSet
from questions.serializers import QuestionsSerializer
from answers.serializers import AnswerSerializers

class QuestionAnswerSerializers(serializers.ModelSerializer):
    question_set = QuestionsSerializer()
    answer_set = AnswerSerializers()

    class Meta:
        model = QuestionsAnswerSet
        fields = ('question_set', 'answer_set')