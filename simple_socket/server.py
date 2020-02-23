import socket
import sys

class socket_server(object):
    def __init__(self, ip):
        self.ip = ip
    # Create a TCP/IP socket

    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to the port
        print(self.ip)
        server_address = (self.ip, 10000)
        print('starting up on {} port {}'.format(*server_address))
        sock.bind(server_address)
        # Listen for incoming connections
        sock.listen(1)
        while True:
            # Wait for a connection
            print('waiting for a connection')
            connection, client_address = sock.accept()
            try:
                print('connection from', client_address)
                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(16)
                    print('received {!r}'.format(data))
                    if data:
                        print('sending data back to the client')
                        connection.sendall(data)
                    else:
                        print('no data from', client_address)
                        break
            finally:
                # Clean up the connection
                connection.close()

class MySocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)