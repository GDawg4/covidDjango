from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from users.views import UsersViewSet
from user_answer.views import UserAnswerViewSet
from questions.views import QuestionsViewSet
from questions_answer_set.views import QuestionAnswerViewSet
from questionnaire_type.views import QuestionnaireViewSet

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'usersanswers', UserAnswerViewSet)
router.register(r'questions', QuestionsViewSet)
router.register(r'questionanswer', QuestionAnswerViewSet)
router.register(r'questionnaire', QuestionnaireViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls))
]
