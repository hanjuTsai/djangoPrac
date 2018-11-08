from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

from uploads.models import Document
from uploads.forms import DocumentForm


@login_required
# Create your views here.
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', locals())

@login_required
def model_form_modify(request):
    command = list(request.POST.keys())
    if request.method == 'POST':
        if len(command) >= 1:
            if 'update' in command:
                id = request.POST.get('update')
                images = Document.objects.filter(id = id) 
                #### confirm the data is deleted
            elif 'upload' in command:
                id = request.POST.get('upload')
                images = Document.objects.filter(id = id) 
                images.delete()
            elif 'delete' in command:
                id = request.POST.get('delete')
                print(id)
                images = Document.objects.filter(id = id) 
                #### confirm the data is deleted
                images.delete() 
                return redirect('products')
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', locals())
