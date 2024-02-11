from django.urls import path

from apps.users.views import UserLogin


app_name = 'users'
urlpatterns = [
    path('login', UserLogin.as_view(), name='users_login'),
]
