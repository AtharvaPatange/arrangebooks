from django.shortcuts import render
from .models import Book
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')



# Create your views here.
