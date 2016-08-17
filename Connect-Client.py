# Connect
# Client Edition
# Alpha 1.0

import socket
import sys
import threading
import tkinter as tk

class listen(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            try: data = server.recv(RECV_BUFFER).decode('utf-8')
            except Exception as e: output('[ERROR] %s'%e)
            output(data, tag='tag-left')

def GUI():
    global root, chatLog, entryBox
    #Root
    root = tk.Tk()
    root.title('Connect (Client)')
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
    entryBox.bind('<Return>', lambda event: entryBox.configure(state='disabled'))
    entryBox.bind('<KeyRelease-Return>', sendMsg)
    #Send Button
    sendButton = tk.Button(root, bd=0, bg='blue', text='Send')
    #Placing Widgets
    chatLog.place(x=10, y=10, height=580, width=455)
    scrollbar.place(x=472, y=13, height=574)
    entryBox.place(x=10, y=595, width=405, height=45)
    sendButton.place(x=420, y=597, width=67, height=41)

def sendMsg(event):
    entryBox.configure(state='normal')
    message = entryBox.get('0.0','end')
    output(message, tag='tag-right')
    server.send(bytes(message, 'utf-8'))
    entryBox.delete('1.0','end-1c')
    chatLog.yview('end')

def output(message, pos='end', tag='tag-center'):
    '''Outputs a message to the GUI'''
    message = str(message)
    if message[-1] != '\n': message += '\n'
    if message[:8] == '[SERVER]':
        tag = 'tag-center'
        message = message[9:]
    chatLog.configure(state='normal')
    chatLog.insert(pos, message, tag)
    chatLog.configure(state='disabled')
    chatLog.yview('end')

GUI()
output('Welcome to Connect!')
output('Connecting...')

HOST = sys.argv[1]
PORT = int(sys.argv[2])
RECV_BUFFER = 4096
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.settimeout(5)
try: server.connect((HOST, PORT))
except Exception: sys.exit()
server.send(bytes(sys.argv[3], 'utf-8'))

output('You are connected to the server!\n')

listen_thread = listen()
listen_thread.start()

root.mainloop()
