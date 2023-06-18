import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Conversation, Message
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from servisarg.models import Trabajador
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def get_room_messages(self):
        messages = await sync_to_async(list)(Message.objects.filter(conversation__room_name=self.room_name).order_by('timestamp'))
        return messages

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
        # Check if conversation exists
        conversation = await database_sync_to_async(Conversation.objects.filter(room_name=self.room_name).first)()
        if not conversation:
            # Create a new conversation if it doesn't exist ejemplo--> 2_1 (idCliente=2 and idTrabajador=1)
            cadena = self.room_name
            partes = cadena.split("_")
            entero1 = int(partes[0])
            entero2 = int(partes[1])
            user_cliente_id = await database_sync_to_async(User.objects.filter(id=entero1).first)()
            user_trabajador_id=await database_sync_to_async(Trabajador.objects.filter(id=entero2).first)()
            conversation = await database_sync_to_async(Conversation.objects.create)( room_name=self.room_name, user1=user_cliente_id, user2=user_trabajador_id)

        # Retrieve existing messages}
        messages = await self.get_room_messages()
       # Send existing messages to the client
        # sender = self.sender # Obtener el valor del remitente del evento

        for message in messages:
            # await self.send(text_data=json.dumps({"message": message.content}))
            await self.send(text_data=json.dumps({"message": message.content, "sender": message.sender}))

        print("enviando mensaje....1")



    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def get_conversation(self):
        conversation = await database_sync_to_async(Conversation.objects.filter(room_name=self.room_name).first)()
        return conversation
    async def create_message(self, conversation, sender, content):
        message = await database_sync_to_async(Message.objects.create)(conversation=conversation, sender=sender, content=content)
        return message
    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]

         # Save message to database
        conversation = await self.get_conversation()
        # TODO setear quien esta enviando el mensaje, por ej: el username del user logeado, esta enviando sender como el emisor y no como
        # todo remitente
        # Create and save the message
        await self.create_message(conversation, sender=username, content=message)
        print("--------------------",message)        

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender": username
            }
        )
        print("enviando mensaje....2")

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]  # Obtener el valor del remitente del evento
        # Enviar mensaje al WebSocket con el remitente
        await self.send(text_data=json.dumps({"message": message, "sender": sender}))
        print("enviando mensaje....3")



