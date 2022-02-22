from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from . import views


app_name = 'home'

urlpatterns = [
	path('', views.home_screen_view, name="home"),

] 