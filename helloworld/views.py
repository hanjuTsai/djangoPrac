from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User

from helloworld.settings import STATICFILES_DIRS
from products.models import Products

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

        print(uploaded_image.title)
        print(uploaded_image.link)
        print(uploaded_image.size)
        print(uploaded_image.type)
        print(uploaded_image.deletehash)
        Products.objects.create(title = uploaded_image.title, link = uploaded_image.link,
            size = uploaded_image.size, filetype = uploaded_image. type, deletehash = uploaded_image.deletehash)

def index(request):
    ## Create a relative path
    img_list = Products.objects.filter().values_list('link',flat=True)
    images = []
    print(type(img_list))
    CLIENT_ID = "af3a88200ef32c0"
    #images.extend(img_list)
    return render(request,'products.html', locals())

def upload(request):
    return render(request,'upload.html')


def home(request):
    return render(request,'home.html')
