from django.urls import path
from django.contrib.auth.urls import views as auth_views

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),

    # Profile
    path('settings/', views.update_user, name='settings'),

    # Password Reset
    path('reset/',
         auth_views.PasswordResetView.as_view(
             template_name='resets/password_reset.html',
             email_template_name='email/password_reset_email.html',
             subject_template_name='email/password_reset_subject.txt'
         ),
         name='password_reset'),
    path('reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='resets/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='resets/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='resets/password_reset_complete.html'),
         name='password_reset_complete'),

    # Password Change
    path('change/',
         auth_views.PasswordChangeView.as_view(template_name='change/password_change.html'),
         name='password_change'),
    path('change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='change/password_change_done.html'),
         name='password_change_done'),
]