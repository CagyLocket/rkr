from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout

from authenticate.forms import RegistrationForm, AccountAuthenticationForm


def register_view(request, *args, **kwargs):
	user = request.user
	if user.is_authenticated: 
		return HttpResponse("You are already authenticated as " + str(user.email))

	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			destination = kwargs.get("next")
			if destination:
				return redirect(destination)
			return redirect('dashboard:index')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'authenticate/register.html', context)


def home(request):
	return render(request, 'authenticate/home.html', {})



def logout_view(request):
	logout(request)
	return redirect("home:home")


def login_view(request, *args, **kwargs):
	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("dashboard:index")

	destination = get_redirect_if_exists(request)
	print("destination: " + str(destination))

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				if destination:
					return redirect(destination)
				return redirect("dashboard:index")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	return render(request, "authenticate/login.html", context)


def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect














# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
# from django.contrib.auth.models import User
# from django.contrib import messages
# from .forms import SignUpForm, EditProfileForm



# def home(request):
# 	return render(request, 'authenticate/home.html', {})


# def login_user(request):
# 	if request.method == "POST":
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(request, username=username, password=password)
# 		if user is not None:
# 			login(request, user)
# 			messages.success(request, f'Hi {username }! You Have Been Logged In!')
# 			return redirect('authenticate:home')
	       
# 		else:
# 			messages.info(request, f'Error - Please Try Again...')
# 			return redirect('authenticate:login')
        
# 	else:
# 		return render(request, 'authenticate/login.html', {})


# def logout_user(request):
# 	logout(request)
# 	messages.success(request, f'You Have Been Logged Out...')
# 	return redirect('authenticate:home')

# def register_user(request):
# 	if request.method == "POST":
# 		form = SignUpForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password1')
# 			user = authenticate(request, username=username, password=password)
# 			login(request, user)
# 			messages.success(request, f'You Have Registered...')
# 			return redirect('authenticate:home')
# 	else:
# 		form = SignUpForm()

# 	context = {'form': form }
# 	return render(request, 'authenticate/register.html', context)


# def edit_profile(request):
# 	if request.method == "POST":
# 		form = EditProfileForm(request.POST, instance=request.user)
# 		if form.is_valid():
# 			form.save()
# 			messages.success(request, f'You Have Edited Your Profile...')
# 			return redirect('authenticate:home')
# 	else:
# 		form = EditProfileForm(instance=request.user)

# 	context = {'form': form }
# 	return render(request, 'authenticate/edit_profile.html', context)


# def change_password(request):
# 	if request.method == "POST":
# 		form = PasswordChangeForm(data=request.POST, user=request.user)
# 		if form.is_valid():
# 			form.save()
# 			update_session_auth_hash(request, form.user)
# 			messages.success(request, f'You Have Changed Your Password...')
# 			return redirect('authenticate:home')
# 	else:
# 		form = PasswordChangeForm(user=request.user)

# 	context = {'form': form }
# 	return render(request, 'authenticate/change_password.html', context)




















