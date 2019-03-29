from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('/')

	return render(request, 'accounts/login.html', {'form' : form})
	
def logout_view(request):
	pass

def signin_view(request):
	pass