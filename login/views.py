from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:
        name = request.user.username
    return render(request,"index.html",locals())

def register(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		email = request.POST.get('email', False)
		# Wrong format
		if name == "" or password == "" or email == "":
			message = "wrong format!"
			return render(request, "register.html", locals())
		try:
			user = User.objects.get(username=name)
		except:
			user = None
		if user is not None:
			message = 'The account is used!'
		else:
			user = User.objects.create_user(name, email, password)
			user.save()
			message = "login success!"
			return render(request, "index.html", locals())
	return render(request, 'register.html', locals())

def login(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=name, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				return redirect('/index/')
				message = 'Hello!'
			else:
				message = 'Your account doesn\'t exist!'
		else:
			message = 'Login Fail!'
	return render(request,"loginPage.html",locals())

def logout(request):
	auth.logout(request)
	return redirect('/index/')
