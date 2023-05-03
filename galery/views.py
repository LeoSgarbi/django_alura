from django.shortcuts import render, get_object_or_404
from galery.models import Photos


def index(request):
    photographys = Photos.objects.order_by("-photo_date").filter(published=True)
    return render(request, 'galery/index.html', {"cards": photographys})

def imagem(request, photo_id):
    photography = get_object_or_404(Photos, pk=photo_id)
    return render(request, 'galery/imagem.html', {"photography": photography})

def searching(request):
    photographys = Photos.objects.order_by("-photo_date").filter(published=True)
    
    if "searching" in request.GET:
        name_searching = request.GET['searching']
        if name_searching:
            photographys = photographys.filter(name__icontains=name_searching)

    return render(request, "galery/searching.html", {"cards": photographys})