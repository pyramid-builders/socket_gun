from simple_socket.client import socket_client

client = socket_client('127.0.0.1')
client.send_message("testmessage")