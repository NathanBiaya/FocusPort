from django.shortcuts import render, get_object_or_404
from .models import Gallery


def home(request):
    galleries = Gallery.objects.all()
    return render(request, 'home.html', {'galleries': galleries})

# This is the Phase 3 logic just added
def gallery_detail(request, slug):
    gallery = get_object_or_404(Gallery, slug=slug)
    photos = gallery.photos.all()
    return render(request, 'gallery_detail.html', {
        'gallery': gallery,
        'photos': photos
    })

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
