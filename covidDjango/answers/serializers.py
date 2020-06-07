from rest_framework import serializers

from answers.models import Answers

class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = (
            'id',
            'code',
            'description',
            'id_father'
        )