import socket
from _thread import *

PORT = 5555
SERVER = socket.gethostbyname(socket.gethostname())
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (SERVER, PORT)
try:
    S.bind(ADDR)
except:
    print("Connection Failed")

S.listen(2)
print("Server is Running: ")

pos = [(0, 0), (100, 100)]

# Creating the thread that is responsible for handling mulitple threads.


def read_pos(str):
    str = str.split(',')
    return int(str[0]), int(str[1])


def make_pos(tup):
    return f"{tup[0]},{tup[1]}"


def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode('utf-8'))
            print("HELLO")
            print(data)
            pos[player] = data

            reply = make_pos(pos[player])
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = make_pos(pos[0])
                else:
                    reply = make_pos(pos[1])

                print(f"Received: {data}")
                print(f"Sending: {reply}")
                conn.sendall(str.encode(reply))
        except:
            break
    conn.close()
    global current_player
    current_player -= 1


# The actual loop that will make the server alive.
current_player = 0
while True:
    conn, addr = S.accept()
    print("Connected to: ", addr)
    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
