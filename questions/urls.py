from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile', views.profile, name='profile'),
    path('users/', views.find_user, name='search'),
    path('users/<str:pk>/', views.user_profile, name='user_profile'),
    path('questions/<int:pk>/delete/', views.delete_question, name='delete_question')
]