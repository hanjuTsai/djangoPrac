from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User

from helloworld.settings import STATICFILES_DIRS
import os

def index(request):
    ## Create a relative path
    p = os.path.join(STATICFILES_DIRS[0],'images')
    img_list = os.listdir(p)
    return render(request, 'board.html', {'images': img_list})

def upload(request):
    return render(request,'upload.html')