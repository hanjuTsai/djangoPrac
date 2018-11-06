from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

from uploads.models import Document
from uploads.forms import DocumentForm


@login_required
# Create your views here.
def model_form_upload(request):
    info = list(request.POST.keys())
    if request.method == 'POST':
        if len(info) >= 1:
            description = info[1]
            images = Document.objects.filter(description = description)
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {
        'form': form , 'images': images
    })
