# Connect
# Server Edition
# Alpha 1.0

import socket
import sys
import threading
import tkinter as tk

class listen(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
            connection, addr = server.accept()
            connections.append(connection)
            while True:
                try:
                    data = connection.recv(RECV_BUFFER).decode('utf-8')
                    peername = connection.getpeername()
                    if peername not in nickname.keys():
                        if data: nickname[peername] = data
                        else: nickname[peername] = 'Anonymous'
                        output('[INFO] Client %s:%s (%s) connected'%tuple(list(addr)+[nickname[peername]]))
                        broadcast(connection, '[SERVER] %s entered the room.'%nickname[peername])
                        continue
                    if data: broadcast(connection, '[%s] %s'%(nickname[peername], data))
                except Exception as e:
                    output('[ERROR] %s'%e)
                    output('[INFO] Client %s:%s (%s) disconnected'%tuple(list(addr)+[nickname[peername]]))
                    broadcast(connection, '[SERVER] %s left the room'%nickname[addr])
                    connection.close()
                    connections.remove(connection)

def GUI():
    global root, chatLog, entryBox
    #Root
    root = tk.Tk()
    root.title('Connect (Server)')
    root.geometry('500x650')
    root.resizable(False, False)
    #Background
    background = tk.Frame(root, bd=0, bg='black')
    background.lower(belowThis=None)
    background.place(x=0,y=0,height=650,width=500)
    #Chat Log
    chatLog = tk.Text(root, bd=0, bg='black', fg='green', cursor='arrow', highlightbackground='black', state='disabled')
    chatLog.tag_configure('tag-center', justify='center')
    chatLog.tag_configure('tag-left', justify='left')
    chatLog.tag_configure('tag-right', justify='right')
    #Srollbar
    scrollbar = tk.Scrollbar(root, command=chatLog.yview)
    chatLog['yscrollcommand'] = scrollbar.set
    #Entry box
    entryBox = tk.Text(root, bd=1, bg='black', fg='green', highlightbackground='green')
    #Send Button
    sendButton = tk.Button(root, bd=0, bg='blue', text='Send')
    #Placing Widgets
    chatLog.place(x=10, y=10, height=580, width=455)
    scrollbar.place(x=472, y=13, height=574)
    entryBox.place(x=10, y=595, width=405, height=45)
    sendButton.place(x=420, y=597, width=67, height=41)

def broadcast(exception_sock, message, newline=True):
    '''Broadcast a message to every connected nodes except for the server and the one who sent the message'''
    if newline and message[-1] != '\n': message += '\n'
    if not isinstance(message, bytes): message = bytes(message, 'utf-8')
    for sock in connections:
        if sock != server and sock != exception_sock:
            try: sock.send(message)
            except Exception: #May be socket disconnection or network problem
                output('[INFO] Client %s:%s (%s) disconnected'%tuple(list(addr)+[nickname[sock.getpeername()]]))
                broadcast(sock, '[SERVER] %s left the room'%nickname[addr])
                sock.close()
                connections.remove(sock)

def output(message, pos='end', tag='tag-center'):
    '''Outputs a message to the GUI'''
    message = str(message)
    if message[-1] != '\n': message += '\n'
    chatLog.configure(state='normal')
    chatLog.insert(pos, message, tag)
    chatLog.configure(state='disabled')
    chatLog.yview('end')

GUI()
output('Welcome to Connect!')
output('Starting...')

HOST = sys.argv[1]
PORT = int(sys.argv[2])
RECV_BUFFER = 4096
MAX_CONNECTIONS = 20
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(MAX_CONNECTIONS)
output('\nChat server started on %s:%d\n'%(HOST, PORT))
connections = [server]
nickname = {}

for i in range(MAX_CONNECTIONS):
    listen_thread = listen()
    listen_thread.start()

root.mainloop()
