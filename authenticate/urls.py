import os
from django.contrib import admin
from django.urls import reverse_lazy
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



app_name = 'authenticate'


urlpatterns = [
	path('login/', views.login_view, name="login"), 
    path('logout/', views.logout_view, name="logout"),
	path('register/', views.register_view, name="register"),
	path('home', views.home, name="home"),



   # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='authenticatepassword_reset/password_change.html'), 
        name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='authenticate/password_reset/password_change_done.html'), 
        name='password_change_done'),



    path('password_reset/confirm/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_confirm.html'),
     name='password_reset_confirm'),

# - PasswordResetDoneView shows a success message for the above
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='authenticate/password_reset/password_reset_done.html'),
     name='password_reset_done'),

# - PasswordResetConfirmView checks the link the user clicked and prompts for a new password
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
# - PasswordResetView sends the mail
    path('password_reset/', auth_views.PasswordResetView.as_view(
         email_template_name = 'authenticate/password_reset/password_reset_email.html', template_name = 'authenticate/password_reset/password_reset_form.html',
        ), name='password_reset'),
 
 # - PasswordResetCompleteView shows a success message for the above  
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='authenticate/password_reset/password_reset_complete.html'),
     name='password_reset_complete'),

]
