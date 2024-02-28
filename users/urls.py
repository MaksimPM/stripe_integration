from django.urls import path
from users.apps import UsersConfig
from users.views import *

app_name = UsersConfig.name

urlpatterns = [
    path('list/', UserListAPIView.as_view(), name='users'),
    path('register/', UserCreateAPIView.as_view(), name='user_register'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user'),
    path('<int:pk>/update/', UserUpdateAPIView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDestroyAPIView.as_view(), name='user_delete')
]
