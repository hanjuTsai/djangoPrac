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

		try:
			user = User.objects.get(username=name)
		except:
			user = None
		if user is not None:
			message = '此使用者已經有人使用'
		else:
			user = User.objects.create_user(name, email, password)
			# user.first_name = 'xxxx'
			# user.last_name = 'xxx'
			# user.is_staff = 'True'
			user.save()
			message = "註冊成功"
			return render(request, "index.html", locals())
	return render(request, 'register.html', locals())

def login(request):
	if request.method == 'POST':   #如果是 <login.html> 按登入鈕傳送
		name = request.POST['username']   #取得表單傳送的帳號、密碼
		password = request.POST['password']
		user = auth.authenticate(username=name, password=password) #使用者驗證
		if user is not None:         #若驗證成功，以 auth.login(request,user) 登入
			if user.is_active:
				auth.login(request,user)
				return redirect('/index/')  #登入成功產生一個 Session，重導到<index.html>
				message = 'Hello!'
			else:
				message = 'Your account doesn\'t exist!'
		else:
			message = 'Login Fail!'
	return render(request,"loginPage.html",locals())  #登入失敗則重導回<login.html>

def logout(request):
	auth.logout(request)  #登出成功清除 Session，重導到<index.html>
	return redirect('/index/')
