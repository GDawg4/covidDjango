from rest_framework import serializers

from questionnaire_type.models import QuestionnaireType
from questions_answer_set.serializers import QuestionAnswerSerializers

class QuestionnaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionnaireType
        fields = ('id', 'description', 'questions')