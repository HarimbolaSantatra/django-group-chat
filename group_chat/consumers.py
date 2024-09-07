# Channels' Consumer
import json

from channels.generic.websocket import WebsocketConsumer

from main.persistance import write as write_data

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    # When receiving a new websocket message from the client
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        # messages: message received
        # Each object should contains the following keys: room, username, message, date
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))
        write_data(text_data_json["room"], text_data_json["username"], text_data_json["message"])

