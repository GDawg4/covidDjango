from rest_framework import serializers

from users.models import Users
from user_answer.serializers import UserAnswerSerializer


class UsersSerializers(serializers.ModelSerializer):
    possible_case = serializers.SerializerMethodField()
    answers_given = UserAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Users
        fields = (
            'id',
            'nametag',
            'useruvg',
            'consent',
            'possible_case',
            'answers_given'
        )

    def get_possible_case(self, obj):
        return sum([True for i in obj.answers_given.get_queryset() if i.id_answer.description == "Si "])