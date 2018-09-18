from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
    return HttpResponse('嗨!,我是蔡涵如，今年資管系大三')
