from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from . import views


app_name = 'dashboard'

urlpatterns = [
	path('', views.index, name="index"),
	path('user_profile/', views.user_profile, name="user_profile"),

] 