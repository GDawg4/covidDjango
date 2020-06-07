from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from users.models import Users
from user_answer.models import UserAnswer
from users.serializers import UsersSerializers
from answers.serializers import AnswerSerializers
from user_answer.serializers import UserAnswerSerializer
from reports.models import Report
from reports.serializers import ReportSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset =  Users.objects.all()
    serializer_class = UsersSerializers

    @action(detail=False, url_path='file', methods=['get'])
    def get_users_file(self, request, pk=None):
        users = Users.objects.all()
        serialized = {}
        for i in range(len(users)):
            user_id = getattr(users[i], 'id')
            serialized[user_id]=UsersSerializers(users[i]).data
            all_answers = UserAnswer.objects.filter(Q(id_user=users[i]))

            file_answers = all_answers.filter(Q(id_questionnaire_type = 2))
            serialized[user_id]['file'] = []
            for file_answer in file_answers:
                serialized[user_id]['file'].append(UserAnswerSerializer(file_answer).data)

            report_answers = all_answers.filter(Q(id_questionnaire_type=1))
            #all_dates = []
            #for report_answer in report_answers:
            #    date = getattr(report_answer, 'report_date')
            #    if date not in all_dates:
            #        all_dates.append(date)
            #        reports = Report.objects.filter(Q(user=user_id), Q(date=date))
            #        if len(reports) == 0:
            #            Report.objects.create(
            #                user = users[i],
            #                date = date,
            #            )

            latest = serialized[user_id]['latest'] = getattr(report_answers.latest('report_date'), 'report_date')
            serialized[user_id]['report'] = []
            recent_report_answers = report_answers.filter(Q(report_date = latest))
            for report_answer in recent_report_answers:
                serialized[user_id]['report'].append(UserAnswerSerializer(report_answer).data)

            latest_report = Report.objects.get(Q(date=latest), Q(user_id=user_id))
            serialized[user_id]['report_status'] = []
            serialized[user_id]['report_status'].append(ReportSerializer(latest_report).data)
        return Response(serialized)
