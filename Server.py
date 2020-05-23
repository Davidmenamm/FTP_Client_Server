
# Server receives pdf files from clients, and changes the name of the files to "file_number.pdf" (i.e.: FileA.pdf)

import socket
sock = socket.socket()
sock.bind(("localhost",9997))
sock.listen(10) # Acepta hasta 10 conexiones entrantes.

extension = '.pdf'

i = 1
while True:
    conn, address = sock.accept()
    # craemos nuevo archivo binario
    file = open( 'file_'+ str(i)
                 + extension,'wb')
    print(address)
    while (True):
        # leemos y escribimos en el fichero
        reader = conn.recv(1024)
        print(reader)
        file.write(reader)

        if not reader:
            break

    file.close()
    conn.close()
    i = i+1

sock.close()