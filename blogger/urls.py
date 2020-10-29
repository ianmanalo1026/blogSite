from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<int:blog_pk>/', views.detail, name='detail'),
    path('signupuser/', views.signupuser, name='signupuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('loginuser/', views.loginuser, name='loginuser'),
    
    path('profile/',views.profile, name='profile'),
    path('profile/createblog/', views.createblog, name='createblog'),
    path('profile/<int:blog_pk>/', views.profiledetail, name='profiledetail'),
    path('profile/<int:blog_pk>/editblog/', views.editblog, name='editblog'),
    path('profile/<int:blog_pk>/deleteblog/', views.deleteblog, name='deleteblog'),
]