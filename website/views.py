from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):
	return render(request, 'login.html')

# @login_required(login_url='/login/')
def admin(request):
	# if request.user.is_authenticated:
	if True:
		return render(request, 'index.html')
	else:
		return redirect('login')