from django.shortcuts import render

def index(request):
    rooms = [{'name':'lobby'}, {'name':'test'}]
    context = {
        'username': '_santatra',
        'rooms': rooms,
        'room_name': '',
    }
    return render(request, 'render/index.html', context)

def room(request, room_name):
    context = {
        'username': '_santatra',
        "room_name": room_name
    }
    return render(request, 'render/room.html', context)