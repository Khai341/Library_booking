import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
#from librarianAdmin.models import Message, Room
from .models import Message, Room
from librarianAdmin.models import Users
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_number = self.scope['url_route']['kwargs']['room_number']
        self.room_group_name = f'chat_{self.room_number}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        #message = text_data_json['message']
        message = text_data_json.get('message', '')
        #sender_user = text_data_json['user']
        sender_user = text_data_json.get('user')
        ##sender_user = None
        rooms = Room.objects.filter(name=self.room_number)
        
        #await self.save_message(rooms.first(), message)#########################
        
        
        # Fetch the Room instance asynchronously
        rooms = await sync_to_async(Room.objects.filter)(number=self.room_number)
        room_instance = await sync_to_async(lambda: rooms.first())()
        
        sender_user1 = await sync_to_async(Users.objects.filter)(username=sender_user)
        user_instance = await sync_to_async(lambda: sender_user1.first())()

        if room_instance:  # Check if room_instance is not None
            # Save the message asynchronously
            await self.save_message(room_instance, message,user_instance)
        else:
            print("Error: Room not found.")
            print(self.room_number)
        
        # Send message to room group  #'room_number': self.room_number
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'room_number': sender_user
            }
        )

    async def chat_message(self, event):
        message = event['message']
        room_number = event['room_number']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': f'{room_number}'  # this will now show correctly
        }))

    @sync_to_async
    def save_message(self, room_number, message,sender_user):
        Message.objects.create(room=room_number, content=message,user=sender_user)
# from channels.generic.websocket import AsyncWebsocketConsumer
# import json
# from .models import Room, Message
# from django.contrib.auth.models import AnonymousUser
# from asgiref.sync import database_sync_to_async

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_number = self.scope['url_route']['kwargs']['room_number']
#         self.room_group_name = f'chat_{self.room_number}'

#         # Try to get the room or reject connection if not found
#         try:
#             self.room = await self.get_room()
#         except Room.DoesNotExist:
#             # Reject the WebSocket connection if the room doesn't exist
#             await self.close()

#         # Join room group
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )

#         await self.accept()

#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         message = data['message']
#         username = self.scope["user"].username if self.scope["user"].is_authenticated else "Guest"

#         # Save the message to the database
#         await self.create_message(self.room, self.scope["user"], message)

#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message,
#                 'username': username
#             }
#         )

#     async def chat_message(self, event):
#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({
#             'message': event['message'],
#             'username': event['username']
#         }))

#     @database_sync_to_async
#     def get_room(self):
#         return Room.objects.get(number=self.room_number)

#     @database_sync_to_async
#     def create_message(self, room, user, content):
#         if user.is_authenticated:
#             return Message.objects.create(room=room, user=user, content=content)
#         else:
#             return Message.objects.create(room=room, user=None, content=content)
