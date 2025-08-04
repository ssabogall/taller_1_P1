from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

def home (request):
    #return render(request, 'home.html', { 'name': 'Santiago Sabogal Lozano' })
    searchTerm = request.GET.get('searchMovie', '')
    if searchTerm:
        Movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        Movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'Movies': Movies })

def about (request):
    return render(request, 'about.html', { 'name': 'Santiago Sabogal Lozano' })

# Create your views here.
