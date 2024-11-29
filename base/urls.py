from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('room/<str:pk>',views.room,name='room'),
    path('create-room/',views.CreateRoom,name='create-room'),
    path('edit-room/<str:pk>',views.EditRoom,name='edit-room'),
    path('delete-room/<str:pk>',views.DeleteRoom,name='delete-room'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('register/',views.Registerpage,name='register'),
    path('delete-message/<str:pk>',views.DeleteMessage,name='delete-message'),
    path('user-profile/<str:pk>',views.userProfile,name='user-profile'),
    path('update-user/',views.updateUser,name='update-user'),
    path('topics/',views.topicsPage,name='topics'),
    path('activity/',views.activityPage,name='activity')
    
]
