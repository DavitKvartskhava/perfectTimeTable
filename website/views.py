from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout

from website.forms import UserLoginForm, UserRegisterForm

# Create your views here.

def index_view(request):
	return render(request, 'index.html')

def login_view(request):
	""" log in user controller"""
	form = UserLoginForm(request.POST or None)

	if form.is_valid():
		username	= form.cleaned_data.get("username")
		password 	= form.cleaned_data.get("password")

		user = authenticate(username = username, password = password)
		login(request, user)
		# print(request.user.is_authenticated())

		return redirect('dashboard')

	return render(request, 'login.html', {"form": form})

def register_view(request):
	# print(request.user.is_authenticated())
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit = False)
		password = form.cleaned_data.get('password1')
		user.set_password(password)
		user.save()
		new_user = authenticate(username = user.username, password = user.password)
		login(request, new_user)
		return redirect('dashboard')

	return render(request, 'register.html', {"form": form})

def logout_view(request):
	""" log out user controller"""
	logout(request)
	return redirect('index')

def dashboard_view(request):
	return render(request, 'index.html')