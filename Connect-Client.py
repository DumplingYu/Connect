# Connect
# Client Edition
# Pre-Alpha 1.0

import socket, select, string, sys

def prompt():
    sys.stdout.write('> ')
    sys.stdout.flush()
    
##if len(sys.argv) < 3:
##    print('Usage: python3 client.py hostname port')
##    sys.exit()

##host = sys.argv[1]
##port = int(sys.argv[2])
SERVER_HOST = 'localhost'
SERVER_PORT = 5550
RECV_BUFFER = 2048

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.settimeout(5)
try: server.connect((SERVER_HOST, SERVER_PORT))
except Exception:
    sys.stdout.write('[ERROR] Unable to connect to remote host\n')
    sys.stdout.flush()
    sys.exit()

sys.stdout.write('[INFO] Connected to remote host\n')
sys.stdout.flush()

while True:
    prompt()
    
    readables = [sys.stdin, server]
    #Get the list of readable sockets
    read_list, write_list, error_list = select.select(readables,[],[])
    
    for sock in read_list:
        if sock == server: #Incoming message from remote server
            data = sock.recv(RECV_BUFFER).decode('utf-8')
            if not data:
                sys.stdout.write('[INFO] Kicked from chat room\n')
                sys.stdout.flush()
                sys.exit()
            else: sys.stdout.write(data)
        else: #User sends a message
            message = bytes(sys.stdin.readline(),'utf-8')
            server.send(message)
