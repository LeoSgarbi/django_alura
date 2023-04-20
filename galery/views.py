from django.shortcuts import render, get_object_or_404
from galery.models import Photos


def index(request):
    photographys = Photos.objects.order_by("photo_date").filter(published=True)
    return render(request, 'galery/index.html', {"cards": photographys})

def imagem(request, photo_id):
    photography = get_object_or_404(Photos, pk=photo_id)
    return render(request, 'galery/imagem.html', {"photography": photography})