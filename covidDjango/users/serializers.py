from rest_framework import serializers

from user_answer.serializers import UserAnswerSerializer
from users.models import Users

class UsersSerializers(serializers.ModelSerializer):
    possible_case = serializers.SerializerMethodField()
    answers_given = UserAnswerSerializer(many=True, read_only=True)
    is_contacted = serializers.BooleanField(default = False)
    is_confirmed = serializers.BooleanField(default=False)

    class Meta:
        model = Users
        fields = (
            'id',
            'nametag',
            'useruvg',
            'consent',
            'possible_case',
            'is_contacted',
            'is_confirmed',
            'answers_given',
        )


    def get_possible_case(self, obj):
        return sum([True for i in obj.answers_given.get_queryset() if i.id_answer.description == "Si "])
