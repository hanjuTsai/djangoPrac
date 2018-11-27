from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User

from helloworld.settings import STATICFILES_DIRS, MEDIA_ROOT
from django.contrib.auth.decorators import login_required

from products.models import Products
from uploads.models import Document

import os
import pyimgur

## Utilty functions
def upload_image(Path):
    CLIENT_ID = "af3a88200ef32c0"
    im = pyimgur.Imgur(CLIENT_ID)

    for i in range(len(Path)) :
        PATH = Path[i]
        title = str(i)
        uploaded_image = im.upload_image(PATH, title=title)
        Products.objects.create(title = uploaded_image.title, link = uploaded_image.link,
            size = uploaded_image.size, filetype = uploaded_image. type, deletehash = uploaded_image.deletehash)

@login_required
def index(request):
    print(request.GET)
    if request.method == "GET":
        word = request.GET.get('search', None)
        if word:
            img_list = Document.objects.filter(description__contains = word)
        else:
            img_list = Document.objects.all()
    else:
        img_list =  Document.objects.all()
    images = []
    images.extend(img_list)
    return render(request,'products.html', locals())

@login_required
def upload(request):
    return render(request,'upload.html')

@login_required
def home(request):
    return render(request,'home.html')
