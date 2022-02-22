from django.shortcuts import render, redirect
from django.http import HttpResponse

# from rkr.models import Farmer


def index(request):
	context = {}
	return render(request, "dashboard/index.html", context)

def user_profile(request):
	# context = {'farmer': Farmer.objects.get()}
	context = {}
	return render(request, "dashboard/user_profile.html", context)

