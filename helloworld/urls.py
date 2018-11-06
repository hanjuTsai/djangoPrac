"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from uploads import views as upv
from login import views as loginpg

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', loginpg.index),

    path('index/', loginpg.index),

    path('login/', loginpg.login , name = 'login'),

    path('accounts/login/', loginpg.login, name = 'login'),

    path('logout/', loginpg.logout),

    path('register/', loginpg.register),

    ## The path show the uploaded files
    path('products/', views.index, name = 'products'),

    ## The path direct to the home page
    path('home/', views.home, name = 'home'),

    path('modify/', upv.model_form_upload),
    ## The path direct to upload page
    path('upload/', upv.model_form_upload , name='upload'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
