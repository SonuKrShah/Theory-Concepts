import pickle
import socket
from _thread import *
from Player import Player

GREEN = (0, 255, 0)
RED = (255, 0, 0)


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

players = [Player(0, 0, 50, 50, RED), Player(100, 100, 50, 50, GREEN)]

# Creating the thread that is responsible for handling mulitple threads.


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print(f"Received: {data}")
                print(f"Sending: {reply}")
                conn.sendall(pickle.dumps(reply))
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
