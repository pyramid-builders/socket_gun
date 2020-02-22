import socket
import select

HEADER_LENGHTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()
socket_list = [server_socket]

clients = {}

def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGHTH)
        if not len(message_header):
            return False
        message_length = int(message_header.decode("utf-8").strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}
    except:
        return False

while True:
    read_sockets, _, exception_sockets = select.select(socket_list, [], socket_list)
    
    for notified_socket in read_sockets:
        if notified_socket ==server_socket:
            client_socket, client_address = server_socket.accept()
            
            user = receive_message(client_socket)
            if user is False:
                continue
            socket_list.append(client_socket)