from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageUploadForm
from .models import File

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def display_image(request, pk):
    image = File.objects.get(pk=pk)
    return HttpResponse(image.file, content_type='image/jpeg')