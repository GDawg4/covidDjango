from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

from questionnaire_type.models import QuestionnaireType
from questionnaire_type.serializers import QuestionnaireSerializer
from questions_answer_set.models import QuestionsAnswerSet
from questions_answer_set.serializers import QuestionAnswerSerializers
from questions.models import Questions
from questions.serializers import QuestionsSerializer
from answers.models import Answers
from answers.serializers import AnswerSerializers
from users.models import Users
from user_answer.models import UserAnswer

class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = QuestionnaireType.objects.all()
    serializer_class = QuestionnaireSerializer

    @action(detail=True, url_path='questions', methods=['GET'])
    def questions(self, request, pk=None):
        sets = QuestionsAnswerSet.objects.all().filter(question_set__id_questionnaire = pk)
        questions = Questions.objects.all().filter(id_questionnaire = pk)
        serialized = []
        for i in range(len(questions)):
            serialized.append(QuestionsSerializer(questions[i]).data)
            serialized[i]['answers'] = []
            possible_answers = QuestionsAnswerSet.objects.all().filter(question_set__id = questions[i].id)
            for answer in possible_answers:
                serialized_answer = AnswerSerializers(answer.answer_set).data
                serialized[i]['answers'].append(serialized_answer)
        return Response(serialized)

    @action(detail=True, url_path='add-answer', methods=['POST'])
    def add_answer(self, request, pk=None):
        questionnaire = self.get_object()
        now = datetime.now()
        new_datetime = now.replace(hour=0, minute=0, second=0, microsecond=0)
        answers = request.data.get('answer')
        user_info = request.data.get('user')
        user = Users.objects.filter(Q(id = user_info))[0]
        answer_99 = Answers.objects.filter(Q(id=99))[0]
        current_questionnaire = QuestionnaireType.objects.filter(Q(id=4))[0]
        for i in answers:
            print('\n',i)
            question_id = Questions.objects.filter(Q(name=i))[0]
            question_type = Questions.objects.filter(Q(name=i)).values('id_question_type')[0]['id_question_type']
            latest_id = UserAnswer.objects.latest('id').id + 1
            #Date
            if question_type == 2:
                UserAnswer.objects.create(
                    id = latest_id,
                    description = answers[i],
                    report_date = new_datetime,
                    id_answer = answer_99,
                    id_questionnaire_type = current_questionnaire,
                    id_questions = question_id,
                    id_user = user
                )
            #Selected
            elif question_type == 3:
                answer_id = Answers.objects.filter(Q(description=answers[i]))[0]
                UserAnswer.objects.create(
                    id=latest_id,
                    description = answer_id,
                    report_date = new_datetime,
                    id_answer = answer_id,
                    id_questionnaire_type = current_questionnaire,
                    id_questions = question_id,
                    id_user = user
                )
            #Textbox
            elif question_type == 4:
                UserAnswer.objects.create(
                    id=latest_id,
                    description=answers[i],
                    report_date=new_datetime,
                    id_answer=answer_99,
                    id_questionnaire_type=current_questionnaire,
                    id_questions=question_id,
                    id_user=user
                )
            #Checked
            elif question_type == 6:
                answer_id = Answers.objects.filter(Q(description=answers[i]))[0]
                UserAnswer.objects.create(
                    id=latest_id,
                    description=answer_id,
                    report_date=new_datetime,
                    id_answer=answer_id,
                    id_questionnaire_type=current_questionnaire,
                    id_questions=question_id,
                    id_user=user
                )
        return Response(status=status.HTTP_200_OK)