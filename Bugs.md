# *Connect* Bugs and Issues

 # | Priority | Platform | Verion | Description | Fixed
:---: | :---: | :---: | :---- | :---- | :---:
1 | *MEDIUM* | Client | Pre-1.0<br>Pre-1.1 | If a new message is recieved while typing, the typed message will disappear. | **YES**<br>Alpha-1.0
2 | *MEDIUM* | Client | Pre-1.0<br>Pre-1.1 | Following up *BUG-1*, Although the message disappears, it will still be stored before the next input. | **YES**<br>Alpha-1.0
3 | LOW | Server | Pre-1.0<br>Pre-1.1<br>Alpha-1.0 | The server will not automatically respond to disconnected clients. | **NO**
4 | *MEDIUM* | Server | Pre-1.0<br>Pre-1.1<br>Alpha-1.0 | The server port sometimes will not close properly. | **NO**
5 | *MEDIUM* | Server | Alpha-1.0 | Unable to close server. | **NO**
6 | LOW | Server | Alpha-1.0 | The 'Send' button and the entry box has no use. | **NO**
7 | LOW | Client | Alpha-1.0 | The 'Send' button has no use. | **NO**
8 | **HIGH** | Client | Alpha-1.0 | Sending special characters like the emoji, will cause the client to lag. | **NO**
9 | *MEDIUM* | Client | Alpha-1.0 | If a nickname includes a space, only the first word will be remained. | **YES**<br>Alpha-2.0
10 | *LOW* | Client | Alpha-1.0 | Users able to spam. | **YES**<br>Alpha-2.0
11 | *MEDIUM* | Client | Alpha-1.0 | Sending a massive chunk of text causes the server to raise a *Bad file descriptor* error. | **NO**
12 | *MEDIUM* | Server | Alpha-1.0 | Server sometimes raises a *Bad file descriptor* error when a client closes the window. | **NO**
