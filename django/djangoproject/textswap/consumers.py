import json
from .models import *
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['recipient_username']
        self.room_group_name = f'chat_{self.room_name}'

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
        message_content = text_data_json['message']
        sender = self.scope["user"]
        recipient_username = self.room_name

        # Save the message to the database using sync_to_async
        create_message = sync_to_async(Message.objects.create)
        message = await create_message(
            sender=sender,
            recipient=await sync_to_async(Auth_user.objects.get)(username=recipient_username),
            content=message_content
        )

        # Send message to room group
        await self.channel_layer.group_send(
            f"inbox_{recipient_username}",
            {
                'type': 'send_message',
                'message': message.content,
                'sender': sender.username,
                'message_id': message.id,
                'is_read': message.is_read
            }
        )
        
        """# Broadcast the message to the recipient's inbox group
        recipient_inbox_group = f"inbox_{recipient_username}"
        await self.channel_layer.group_send(
            recipient_inbox_group,
            {
                'type': 'send_message',
                'message': message.content
            }
        )"""

    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': self.scope["user"].username
        }))

class InboxConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.inbox_group_name = f"inbox_{self.user.username}"

        await self.channel_layer.group_add(
            self.inbox_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.inbox_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle any incoming messages (if needed)
        pass

    async def send_message(self, event):
        print(event)
        message = event['message']
        sender = event['sender']
        message_id = event['message_id']
        is_read = event['is_read']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'message_id': message_id,
            'is_read': is_read
        }))