from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from users.views import UsersViewSet
from user_answer.views import UserAnswerViewSet

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'usersanswers', UserAnswerViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls))
]
