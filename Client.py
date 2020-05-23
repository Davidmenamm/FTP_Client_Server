
# client sends a pdf file to server

import socket
import tkinter
import tkinter.filedialog

root = tkinter.Tk() # Tkinter Root Class
port = 9997
ip = "localhost"

def print_path():
    path_given = tkinter.filedialog.askopenfilename(
        parent=root, initialdir='C:/Tutorial',
        title='Choose file',
        filetypes=[('png images', '.png'),
                   ('gif images', '.gif'),
                   ('pdf files', '.pdf'),
                   ('jpg images', '.jpg')]
        )


    sock = socket.socket()
    sock.connect((ip, port))

    file = open (path_given, "rb")
    reader = file.read(1024)

    while(reader):
        sock.send(reader)
        reader = file.read(1024)
        print(reader)
        if not reader:
            file.close()
            sock.close()
            break

b1 = tkinter.Button(root, text='Print path', command=print_path)
b1.pack(fill='x')

root.mainloop()