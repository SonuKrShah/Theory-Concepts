import socket
from _thread import *

# This sections contains the variables and declarations of setting the socket
PORT = 5555
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)

S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ADDR = (SERVER, PORT)
print(ADDR)
try:
    S.bind(ADDR)
except:
    print("Connection Failed")


S.listen(2)
print("Waiting for the connection, server started: ")


def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')

            if not data:
                print("Disconnected")
                break
            else:
                print(f"Received: {reply}")
                print(f"Sending: {reply}")
            conn.sendall(str.encode(reply))
        except:
            break
    print("Lost Connection")
    conn.close()


while True:
    # Accept connections
    conn, addr = S.accept()
    print("Connected To: ", addr)

    start_new_thread(threaded_client, (conn, ))
