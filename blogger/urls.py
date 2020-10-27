from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<int:blog_pk>/', views.detail, name='detail'),
    path('signupuser/', views.signupuser, name='signupuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('createblog/', views.createblog, name='createblog'),
]