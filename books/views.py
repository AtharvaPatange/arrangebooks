from django.shortcuts import render
from .models import Room


# rooms=[
#     {'id':1, 'name':"Let's learn python!"},
#     {'id':2, 'name':"Let's learn Django!"},
#     {'id':3, 'name':"Let's learn Javascript!"},

# ]

# You can render data like this {'rooms':rooms}
# def home(request):
#     return render(request, 'home.html',{'rooms':rooms})
def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'books/home.html', context) 

def room(request,pk):
    room = Room.objects.get(id=pk)
    context= {'room':room}
    return render(request, 'books/room.html',context)



# Create your views here.
