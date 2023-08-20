import main.persistance

from datetime import datetime, timedelta

class User():
    def __init__(self, name):
        self.username = name


class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = "Random description"


class Chat():
    def __init__(self, id):
        self.chat = persistance.get_by_id(id)
        self.message = chat.message
        self.user = chat.username
        self.room = chat.room
        self.date = datetime.fromisoformat(chat.date)

    def get_day(self):
        return self.date.strftime("%b %d")

    def get_time(self, tz=0):
        # tz: time delta for a time zone
        delta = timedelta(hours=tz)
        f_time = self.date + delta
        return f_time.strftime("%I:%M %p")


    @staticmethod
    def sort_chats_per_day_per_hour(chats, current_username):
        """
        Return a good representation of chat objects

        Parameters:
        -----------
        chats: list
            list of Chat objects
        current_username: str
            current username

        Return:
        -----------
        chat_per_day: complex nested list of dictionary, in format:
            [
                { 
                    "day" : "Month 07",
                    "per_hour" : [
                        { 
                            "hour": "14:08 PM",
                            "chats": [
                                { 
                                    "username": "my_username", 
                                    "message": <Chat.message>,
                                    "time": "14:08 PM",
                                    "class_name": "<primary|secondary>-message-row"
                                },
                                {
                                    ...    
                                }
                            ]
                        },
                        {
                            ...
                        }
                    ]
                },
                {
                    ...
                }
            ]

        """
        
        chat_per_day = []
        current_day = None
        current_hour = None
        last_username = None  # use for hiding same consecutive username
        for chat in chats:

            mdg_time = chat.get_time(tz=3)  # Madagascar time zone is UTC+3

            isOwner = (chat.user.username == current_username)
            class_name = "primary-message-row" if isOwner else "secondary-message-row"

            # style_username: show username only if message owner is not current logged user
            if isOwner or last_username == chat.user.username:
                style_username = ""
            else:
                style_username = chat.user.username
            last_username = chat.user.username

            new_chat = { 
                "username":style_username, 
                "message":chat.message,
                "time":mdg_time,
                "class_name": class_name
                }

            # Sort chat messages per day
            if current_day == None or current_day != chat.get_day():
                current_day = chat.get_day()
                chat_per_day.append({"day": current_day, "per_hour": []})

            # Sort messages per hour
            if current_hour == None or current_hour != mdg_time:
                current_hour = mdg_time
                chat_per_day[-1]['per_hour'].append({"hour": current_hour, "chats": [new_chat]})
            else:
                chat_per_day[-1]['per_hour'][-1]["chats"].append(new_chat)


        return chat_per_day
