# Connect
# Server Edition
# Pre-Alpha 1.1

import socket, select, sys

def broadcast(exception_sock, message, newline=True):
    '''Broadcast a message to every connected nodes except for the server and the one who sent the message'''
    if newline and message[-1] != '\n': message += '\n'
    if not isinstance(message, bytes): message = bytes(message, 'utf-8')
    for sock in connections:
        if sock != server and sock != exception_sock:
            try: sock.send(message)
            except Exception: #May be socket disconnection or network problem
                write('[INFO] Client %s:%s (%s) disconnected'%tuple(list(addr)+[nickname[sock.getpeername()]]))
                broadcast(sock, '\n\r[SERVER] %s left the room'%nickname[addr])
                sock.close()
                connections.remove(sock)

def write(message, newline=True):
    '''Outputs a message to the server terminal'''
    message = str(message)
    if newline and message[-1] != '\n': message += '\n'
    sys.stdout.write(message)
    sys.stdout.flush()

write('[CONNECT] Welcome to Connect!')

write('[CONNECT] Please input the host: ', False)
host = sys.stdin.readline().strip()
if not host: host = 'localhost'
while True:
    write('[CONNECT] Please input the port: ', False)
    port = sys.stdin.readline().strip()
    if not port: port = 2189
    try:
        port = int(port)
        break
    except ValueError:
        write('[ERROR] Invalid Input!')
RECV_BUFFER = 2048
MAX_CONNECTIONS = 20
connections = []
nickname = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(MAX_CONNECTIONS)
connections.append(server)
write('[INFO] Chat server started on port %d'%PORT)

while True:
    try:
        #Get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(connections,[],[])

        for sock in read_sockets:
            if sock == server: #New connection through server socket
                connection, addr = server.accept()
                connections.append(connection)
             
            else: #Incoming message from a client
                try:
                    data = sock.recv(RECV_BUFFER).decode('utf-8')
                    peername = sock.getpeername()
                    if peername not in nickname.keys():
                        if data: nickname[peername] = data[:-1]
                        else: nickname[peername] = 'Anonymous'
                        write('[INFO] Client %s:%s (%s) connected'%tuple(list(addr)+[nickname[peername]]))
                        broadcast(connection, '\n\r[SERVER] %s entered the room\n'%nickname[peername])
                        continue
                    if data:
                        broadcast(sock, '\n\r[%s] %s'%(nickname[peername], data))
                except Exception as e:
                    print(e)
                    write('[INFO] Client %s:%s (%s) disconnected'%tuple(list(addr)+[nickname[peername]]))
                    broadcast(sock, '\n\r[SERVER] %s left the room'%nickname[addr])
                    sock.close()
                    connections.remove(sock)
    except KeyboardInterrupt:
        write('\b\b[INFO] Server closing...')
        broadcast(server, '\n[SERVER] Chat room closed by server')
        break
server.close()
write('[INFO] Server closed')
sys.exit()
