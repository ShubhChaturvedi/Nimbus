from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signUp"),
    path('logout', views.logout, name="logout"),
    path('forgotPwd', views.forgotPwd, name="forgotPwd"),
]