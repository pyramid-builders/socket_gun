from simple_socket.server import *

server = socket_server('127.0.0.1')
server.start()

mysock = MySocket