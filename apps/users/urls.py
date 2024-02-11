from django.urls import path

from apps.users.views import UserLogin, UserRegister

app_name = 'users'
urlpatterns = [
    path('login', UserLogin.as_view(), name='users_login'),
    path('signup', UserRegister.as_view(), name='users_signup'),
]
