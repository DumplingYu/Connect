# Connect
# A Python-based chat room
# Server Edition
# Pre-Alpha 1.0

import socket, select, sys

sys.stdout.write('[INFO] Welcome to Connect!\n')
sys.stdout.flush()

def broadcast(exception_sock, message):
    if not isinstance(message, bytes): message = bytes(message, 'utf-8')
    for sock in connections:
        if sock != server and sock != exception_sock:
            try: sock.send(message)
            except Exception: #May be socket disconnection or network problem
                sys.stdout.write('[INFO] Client %s:%s disconnected\n'%addr)
                sys.stdout.flush()
                broadcast(sock, '\b\b[SERVER] %s:%s left the room\n'%addr)
                sock.close()
                connections.remove(sock)

HOST = 'localhost'
PORT = 5550
RECV_BUFFER = 2048
MAX_CONNECTIONS = 20
connections = []
nickname = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(MAX_CONNECTIONS)
connections.append(server)
sys.stdout.write('[INFO] Chat server started on port %d\n'%PORT)
sys.stdout.flush()

while True:
    try:
        #Get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(connections,[],[])

        for sock in read_sockets:
            if sock == server: #New connection through server socket
                connection, addr = server.accept()
                connections.append(connection)
                sys.stdout.write('[INFO] Client %s:%s connected\n'%addr)
                sys.stdout.flush()
                broadcast(connection, '[SERVER] %s:%s entered the room\n'%addr)
             
            else: #Incoming message from a client
                try:
                    data = sock.recv(RECV_BUFFER).decode('utf-8')
                    if data:
                        broadcast(sock, '\r[%s:%d] %s'%tuple(list(sock.getpeername())+[data]))
                except Exception as e:
                    print(e)
                    sys.stdout.write('[INFO] Client %s:%s disconnected\n'%addr)
                    sys.stdout.flush()
                    broadcast(sock, '\b\b[SERVER] %s:%s left the room\n'%addr)
                    sock.close()
                    connections.remove(sock)
    except KeyboardInterrupt:
        sys.stdout.write('\b\b[INFO] Server closing...\n')
        sys.stdout.flush()
        broadcast(server, '[SERVER] Chat room closed by server\n')
        break
server.close()
sys.stdout.write('[INFO] Server closed\n')
sys.stdout.flush()
sys.exit()
