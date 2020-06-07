from rest_framework import serializers

from questions.models import Questions

class QuestionsSerializer(serializers.ModelSerializer):
    id_question_type = serializers.StringRelatedField(many=False, read_only=True)
    #id_sections=serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Questions
        fields = (
            'id',
            'name',
            'title',
            'correlative',
            'id_question_type',
            'id_questionnaire',
            'display',
            'image',
            'id_sections'
        )