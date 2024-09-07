from django.http import JsonResponse
from django.shortcuts import render, redirect

from main.models import Room
from . import persistance

def index(request):
    """The login page"""
    rooms = [{'name':'test'}, {'name':'lobby'}]
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
    request.session.clear()
    return redirect(f'/')


def load_messages(request, room_name):
    """
    Take a request and return a json response containing the next message.
    Parameters:
        request
        room_name: str
    Return:
        json containing a list
    """

    MESSAGE_PER_PAGE = 5

    # check if a request have already been done. Update the index accordingly
    if 'current_index' not in request.session or request.session['current_index'] == None:
        l = persistance.get_length(room_name)  # length of the data
        # initial-index = len(set) - len(subset)
        request.session['current_index'] = l - MESSAGE_PER_PAGE

    # if current_index is negative, do not get more message anymore
    ci = request.session['current_index'] 

    # check if user is not logged in or if username is empty
    if 'username' not in request.session or request.session['username'] == "" :
        return redirect('index')

    response = persistance.get_room_paginated(room_name, MESSAGE_PER_PAGE, ci)
    request.session['current_index'] = ci - MESSAGE_PER_PAGE 

    return JsonResponse({"data" : response})


def room(request, room_name):
    """Room page where user talks to each other"""
    # if user is not connected
    if 'username' not in request.session:
        return redirect(f'/')

    current_room = Room(room_name)

    # on first load or on reload, clear session[current_index]
    if 'current_index' in request.session:
        request.session['current_index'] = None

    context = {
        "username": request.session['username'],
        "room_name": room_name,
    }
    return render(request, 'main/room.html', context)


def write(request):
    # Take a POST request to write to the data.json file
    status = 0
    if request.method == "POST":
        # if all the request data is present, do the operation
        if 'room' in request.POST and 'username' in request.POST and 'message' in request.POST:
            data = {
                'room' : request.POST.get('room'),
                'username' : request.POST.get('username'),
                'message' : request.POST.get('message')
            }
            # Write to the JSON file
            persistance.write(**data)
            status = 200
        else:
            status = 400
            raise Exception("Tsy afaka alefa ireo data fa misy banga ny payload !")
    return JsonResponse({"status" : status})

