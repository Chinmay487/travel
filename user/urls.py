from django.urls import path
from . import views

urlpatterns = [
    path('login_auth',views.login_auth,name='login_auth'),
    path('',views.loginPage,name='loginPage')
]