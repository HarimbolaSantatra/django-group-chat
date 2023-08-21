from django.http import JsonResponse
from django.shortcuts import render, redirect

import json

from . import persistance
from main.models import User, Room, Chat

def index(request):
    rooms = [{'name':'lobby'}, {'name':'test'}]
    context = {
        'username': '',
        'rooms': rooms,
        'room_name': '',
    }

    # If already logged in, login page in not available anymore
    if 'username' in request.session:
        return render(request, 'main/room.html', context)

    # On form submit
    if request.method == "POST":
        
        # if username is empty, return to index
        if request.POST.get('username') == "":
            return redirect('index')

        # save POST request
        username = request.POST.get('username')
        roomname = request.POST.get('room_name')

        request.session['username'] = username
        request.session['room_name'] = roomname
        context['username'] = username
        context['room_name'] = roomname
        return redirect(f'/room/{roomname}')

    
    return render(request, 'main/index.html', context)


def logout(request):
    rooms = [{'name':'lobby'}, {'name':'test'}]
    context = {
        'username': '',
        'rooms': rooms,
        'room_name': '',
    }
    request.session.clear()
    return redirect(f'/')


def load_messages(request, room_name):
    """
    Take a request and return a json response containing the next message.
    """

    MESSAGE_PER_PAGE = 4

    try:
        ci = request.session['current_index']
    except KeyError:
        request.session['current_index'] = 0
        ci = 0

    username = request.session['username']

    # Query a number of chat message. Invert sort by date
    # We extract the chat object in reverse order so notice how we index the result
    # due to UI implementation, we must reverse the order of the result
    chats = persistance.get_room(room_name)[ci:MESSAGE_PER_PAGE+ci]
    chats = Chat.convertList(chats)

    # # update message index
    request.session['current_index'] = ci + MESSAGE_PER_PAGE

    response = {
        'username': username,
        'room_name': room_name,
        'chat_per_day': Chat.sort_chats_per_day_per_hour(chats, username),
        
        # just for debugging and knowing the request status
        'ci': ci,
        'session_index': request.session['current_index'],
    }

    return JsonResponse(response)


def room(request, room_name):
    # if user is not connected
    if 'username' not in request.session:
        return redirect(f'/')

    current_room = Room(room_name)
    context = {
        "username": request.session['username'],
        "room_name": room_name,
        "chats": persistance.get_room(room_name),
    }
    return render(request, 'main/room.html', context)