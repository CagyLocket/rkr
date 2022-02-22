from django.shortcuts import render

# Create your views here.

def farm_identification_data_screen_view(request):
	context = {}
	return render(request, "rkr/farm_identification_data.html", context)
