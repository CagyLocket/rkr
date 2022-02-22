from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from . import views


app_name = 'rkr'

urlpatterns = [
	path('dashboard/farm/identification_data/', views.farm_identification_data_screen_view, name="farm_identification_data"),

] 