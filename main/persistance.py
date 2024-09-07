# All the models here are custom models, since we are using a flat-file database
import os, json
from datetime import datetime

parent_dir = os.path.join(os.path.dirname(__file__), os.pardir)
dataPath = os.path.join(parent_dir, 'data.json')


def open_data(mode='r'):
    """Read data file and return a python object

       Args:
            mode -- read mode
    
       Returns:
            object of format {"0": {...}, ...}
    """
    data = {}
    with open(dataPath, mode) as file:
        data = json.load(file)
    return data


def get_last_index():
	"""Return the index after the last index"""
	data = open_data()
	i = 0
	while True:
		if str(i) in data.keys():
			# if i in the keys, last not reached yet
			i += 1
		else:
			break  # just to be safe that the loop will end
	return i

def get_length(room_name=""):
    """ Return the length of the data. If no room name is specified, return the total number.
    Parameter: room_name: str, optional
    Return: length
    """
    if room_name == "" or room_name == None:
        data = open_data()
        return len(data.values())
    else:
        data = get_room(room_name)
        return len(data)

def get_room(room_name):
	""" Return the messages in a given room name
	Parameter:
		room_name (str)
	Return:
		data: list of object
	"""
	data = open_data()
	result = [ e for e in data.values() if e["room"] == room_name]
	return result


def get_room_paginated(room_name, nb, index):
    """ Get specific number of message in a room.
    Parameter:
        room_name
        nb: number of message to extract
        index: begin to get message at this specific index
    Return:
        data: list of object. Each object must contains the following keys: room, username, message, date
    """
    data = get_room(room_name)
    offset = 0 if (nb + index) < 0 else nb + index
    # if index < 0, just get the remaining item
    index = 0 if index < 0 else index
    # subset return a list of object
    subset = data[ index : offset ]
    return subset


def get_by_id(id):
	r = {}
	data = open_data()
	for k in data.keys():
		if int(k) == id:
			r = data[k]
	return r


def write(room, username, message, date=datetime.now()):
	"""Write to the data.json. All parameters are string."""
	data = open_data()
	last_index = get_last_index()
	data[last_index] = {
		"room": str(room),
		"username": str(username),
		"message": str(message),
		"date": str(date),
	}
	with open(dataPath, "r+") as file:
		# clear the whole file first
		file.truncate(0)
		# copy data inside the file
		json.dump(data, file)
	
