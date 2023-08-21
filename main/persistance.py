# All the models here are custom models, since we are using a flat-file database
import os, json
from datetime import datetime

parent_dir = os.path.join(os.path.dirname(__file__), os.pardir)
dataPath = os.path.join(parent_dir, 'data.json')

def open_data(mode='r'):
	data = {}
	with open(dataPath, mode) as file:
		data = json.load(file)
	return data


def get_last_index():
	data = open_data()
	i = 0
	while True:
		if str(i) in data.keys():
			# if i in the keys, last not reached yet
			i += 1
		else:
			break  # just to be safe that the loop will end
	return i


def get_all():
	all = []
	data = open_data()
	for element in data.values():
		all.append(element)
	return all


def get_room(room_name):
	all = []
	data = open_data()
	for element in data.values():
		if element['room'] == room_name:
			all.append(element)
	return all


def get_by_id(id):
	r = {}
	data = open_data()
	for k in data.keys():
		if int(k) == id:
			r = data[k]
	return r


def write(room, username, message, date=datetime.now()):
	"""
	Write to the data.json
	"""
	data = open_data()
	last_index = get_last_index()
	data[last_index] = {
		"room": str(room),
		"username": str(username),
		"message": str(message),
		"date": str(date),
	}
	with open(dataPath, "r+") as file:
		json.dump(data, file)

	