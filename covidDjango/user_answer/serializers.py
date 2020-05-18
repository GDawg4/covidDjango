from rest_framework import serializers

from user_answer.models import UserAnswer
from questions.serializers import QuestionsSerializer

class UserAnswerSerializer(serializers.ModelSerializer):
    id_questions = serializers.StringRelatedField(many=False)
    id_answer = serializers.StringRelatedField(many=False)

    class Meta:
        model = UserAnswer
        fields = (
            'id_questions',
            'id_answer'
        )