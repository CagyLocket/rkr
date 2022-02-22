from django.shortcuts import render, redirect
from django.http import HttpResponse

from demo.models import Farmer


def farm(request):
	context = {}
	return render(request, "demo/pages/farm.html", context)

def farm_code_system(request):
	context = {"n": range(5)}
	return render(request, "demo/farm_code_system.html", context)

def farm_id_data(request):
	context = {}
	return render(request, "demo/farm_id_data.html", context)

def farmer_id_data(request):
	Farmers = Farmer.objects.filter(farmer=request.user)
	context = {'Farmers': Farmers}
	return render(request, "demo/farmer_id_data.html", context)


def t00_uwagi(request):
	context = {}
	return render(request, "demo/pages/t00_uwagi.html", context)

def t01_siedlisko(request):
	context = {}
	return render(request, "demo/pages/t01_siedlisko.html", context)

def t02_szkic_pol(request):
	context = {}
	return render(request, "demo/pages/t02_szkic_pol.html", context)

def t1_1_opis_ziemi_wlasnej(request):
	context = {}
	return render(request, "demo/pages/t1_1_opis_ziemi_wlasnej.html", context)

def t1_2_opis_ziemi_dzierzawionej(request):
	context = {}
	return render(request, "demo/pages/t1_2_opis_ziemi_dzierzawionej.html", context)

def t1_3_ziemia_jakosc_i_uzytkowanie(request):
	context = {}
	return render(request, "demo/pages/t1_3_ziemia_jakosc_i_uzytkowanie.html", context)

def t1_4_melioracje(request):
	context = {}
	return render(request, "demo/pages/t1_4_melioracje.html", context)

def t1_5_sady_inne_plantacje(request):
	context = {}
	return render(request, "demo/pages/t1_5_sady_inne_plantacje.html", context)

def t1_6_lasy_i_zadrzewienia(request):
	context = {}
	return render(request, "demo/pages/t1_6_lasy_i_zadrzewienia.html", context)

def t2_wartosci_niemat_i_prawne(request):
	context = {}
	return render(request, "demo/pages/t2_wartosci_niemat_i_prawne.html", context)




















