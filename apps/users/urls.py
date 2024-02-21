from django.urls import path

from apps.users.views import UserLogin, UserRegister, UsersLogoutView

app_name = 'users'
urlpatterns = [
    path('login', UserLogin.as_view(), name='users_login'),
    path('signup', UserRegister.as_view(), name='users_signup'),
    path('logout', UsersLogoutView.as_view(), name='users_logout'),
]
