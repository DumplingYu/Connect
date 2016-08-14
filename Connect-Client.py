# Connect
# Client Edition
# Pre-Alpha 1.1

import socket, select, sys

def prompt():
    '''User input message'''
    write('> ', False)

def write(message, newline=True):
    '''Outputs a message to the terminal'''
    message = str(message)
    if newline and message[-1] != '\n': message += '\n'
    sys.stdout.write(message)
    sys.stdout.flush()

write('[CONNECT] Welcome to Connect!')

write('[CONNECT] Please input the host: ', False)
server_host = sys.stdin.readline().strip()
if not server_host: server_host = 'localhost'
while True:
    write('[CONNECT] Please input the port: ', False)
    server_port = sys.stdin.readline().strip()
    if not server_port: server_port = 2189
    try:
        server_port = int(server_port)
        break
    except ValueError:
        write('[ERROR] Invalid Input!')
RECV_BUFFER = 2048

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.settimeout(5)
try: server.connect((server_host, server_port))
except Exception:
    write('[ERROR] Unable to connect to remote host')
    sys.exit()
write('[CONNECT] Please input your nickname for this chat: ', False)
nickname = bytes(sys.stdin.readline(),'utf-8')
server.send(nickname)
write('[INFO] You have joined the chat room')

while True:
    prompt()
    
    readables = [sys.stdin, server]
    #Get the list of readable sockets
    read_list, write_list, error_list = select.select(readables,[],[])
    
    for sock in read_list:
        if sock == server: #Incoming message from remote server
            data = sock.recv(RECV_BUFFER).decode('utf-8')
            if not data: #Server closed or kicked
                write('\r[INFO] Kicked from chat room')
                sys.exit()
            else: sys.stdout.write(data)
        else: #User sends a message
            message = bytes(sys.stdin.readline(),'utf-8')
            server.send(message)
