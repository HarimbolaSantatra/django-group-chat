# All the models here are custom models, since we are using a flat-file database
import os
import json

parent_dir = os.path.join(os.path.dirname(__file__), os.pardir)
dataPath = os.path.join(parent_dir, 'data.json')
data = {}

with open(dataPath, 'r') as file:
	data = json.load(file)

def get_all():
	all = []
	for element in data.values():
		all.append(element)
	return all


def get_room(room_name):
	all = []
	for element in data.values():
		if element['room'] == room_name:
			all.append(element)
	return all


def get_by_id(id):
	r = {}
	for k in data.keys():
		if int(k) == id:
			r = data[k]
	return r
