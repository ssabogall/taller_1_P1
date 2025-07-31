from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return render(request, 'home.html', { 'name': 'Greg Lim' })

def about (request):
    return HttpResponse("About Page")

# Create your views here.
