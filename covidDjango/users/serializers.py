from rest_framework import serializers

from user_answer.serializers import UserAnswerSerializer
from users.models import Users

class UsersSerializers(serializers.ModelSerializer):
    #possible_case = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = (
            'id',
            'nametag',
            'useruvg',
            'consent'
            #'possible_case'
        )

    #def get_possible_case(self, obj):
        #return sum([True for i in obj.answers_given.get_queryset() if i.id_answer.description == "Si "])

