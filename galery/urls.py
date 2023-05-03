from django.urls import path
from galery.views import index, imagem, searching

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:photo_id>', imagem, name='imagem'),
    path("searching", searching, name="searching")
]