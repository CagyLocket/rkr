from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from . import views


app_name = 'demo'

urlpatterns = [
	path('farm/', views.farm, name="farm"),
	path('farm/farm_code_system/', views.farm_code_system, name="farm_code_system"),
	path('farm/farm_id_data/', views.farm_id_data, name="farm_id_data"),
	path('farm/farmer_id_data/', views.farmer_id_data, name="farmer_id_data"),
	path('majatek_trwaly/aktywa/t0_0/uwagi/', views.t00_uwagi, name="t00_uwagi"),
	path('majatek_trwaly/aktywa/t0_1/siedlisko/', views.t01_siedlisko, name="t01_siedlisko"),
	path('majatek_trwaly/aktywa/t0_2/szkic_pol/', views.t02_szkic_pol, name="t02_szkic_pol"),
	path('majatek_trwaly/aktywa/t1_1/opis_ziemi_wlasnej/', views.t1_1_opis_ziemi_wlasnej, name="t1_1_opis_ziemi_wlasnej"),
	path('majatek_trwaly/aktywa/t1_2/opis_ziemi_dzierzawionej/', views.t1_2_opis_ziemi_dzierzawionej, name="t1_2_opis_ziemi_dzierzawionej"),

	
	path('majatek_trwaly/aktywa/t1_3/ziemia_jakosc_i_uzytkowanie/', views.t1_3_ziemia_jakosc_i_uzytkowanie, name="t1_3_ziemia_jakosc_i_uzytkowanie"),
	path('majatek_trwaly/aktywa/t1_4/melioracje/', views.t1_4_melioracje, name="t1_4_melioracje"),
	path('majatek_trwaly/aktywa/t1_5/sady_inne_plantacje/', views.t1_5_sady_inne_plantacje, name="t1_5_sady_inne_plantacje"),
	path('majatek_trwaly/aktywa/t1_6/lasy_i_zadrzewienia/', views.t1_6_lasy_i_zadrzewienia, name="t1_6_lasy_i_zadrzewienia"),
	path('majatek_trwaly/aktywa/t2_0/wartosci_niemat_i_prawne/', views.t2_wartosci_niemat_i_prawne, name="t2_wartosci_niemat_i_prawne"),

] 

