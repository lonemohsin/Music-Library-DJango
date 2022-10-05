from django.http import HttpResponse
from django.template import loader
from .models import Album

def index(request):
    return HttpResponse("<h2>This will be the list of all albums:</h2>")

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")