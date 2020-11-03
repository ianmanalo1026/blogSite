from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<int:blog_pk>/', views.detail, name='detail'),
    path('signupuser/', views.signupuser, name='signupuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('loginuser/', views.loginuser, name='loginuser'),
    
    path('mypage/',views.mypage, name='mypage'),
    path('mypage/my_profile/', views.my_profile, name='my_profile'),
    path('mypage/my_profile/my_profile_update', views.my_profile_update, name='my_profile_update'),
    path('mypage/createblog/', views.createblog, name='createblog'),
    path('mypage/<int:blog_pk>/', views.viewblog, name='viewblog'),
    path('mypage/<int:blog_pk>/editblog/', views.editblog, name='editblog'),
    path('mypage/<int:blog_pk>/deleteblog/', views.deleteblog, name='deleteblog'),
]

