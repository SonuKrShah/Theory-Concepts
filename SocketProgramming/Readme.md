# Socket Programming Reference

### How online games work:

We have multiple clients connecting to one server(main location).

Eg: Online chess game. Where the two players are the clients and the server connects them for playing the game.

The client will be sending and receiving information whereas the server will be responsible for handling the communication of these clients over these two networks.

## Things included in this reference.

- How client and server works and how to create them.
- Deploying things to an external server.
- Working with linux server to deploy our game.
- Working with local host.

## Networking Paradigms

Gaming is an example of client server model.
A game has a central server and the various players are the clients.

- **Client :** A client is the instance of your game running on your computer.

#### Client Server Model

![Client Server Model](https://msatechnosoft.in/blog/wp-content/uploads/2017/04/Client-Server-Architecture-MSA-Technosoft.png)

This central model is much secure and faster and efficient. Eg. if you are playing with 100 players then it's not feasible to connect to all of them.

Here, the server is responsible to handle the communication between the clients.

> Eg: A character wants to move to the right

- This info is passed to the server with some kind of command/message protocol
- To make sure that the client is not cheating. To do this, the server can check the previous state, speed and make sure the client is sending accurate information.

- Now the server transmits the message over to all the clients.

### Setting up the basic client server model.

Here we are using pygame module for the graphics but you can use Tkinter as well for the graphics.

**Modules Used**

```python
import socket
import thread
import sys
# Here we will be using socket and threading to handle connections to our server.
```

Here we will be setting up the socket that will allow for connections to come into a certain port.

**Setting Up the Socket**

```python
PORT = 5555 #You can use any port
# To get the local IP address of the system
SERVER = socket.gethostbyname(socket.gethostname())

S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Here AF_INET means What is the type of connection that this socket will be accepting, It represents IPv4 address.
# SOCK_STREAM means what we are streaming via the socket. It represents TCP connection.
```

For binding the PORT and SERVER to the socket

For this, we use a tuple where the first element is the IP address and the second in PORT number.

```python
# It's a good practice to include this in a try catch block
ADDR = (SERVER, PORT)
S.bind(ADDR)
```

**To Open the port for accepting connections**

`S.listen(No_of_Connections_allowed)`

Note: If you leave the argument blank, then unlimited connections are possible.

For accepting the connections to the server

```python
while True:
    # Accept connections
    conn, addr = S.accept()
    print("Connected To: ", addr)

    # This is used to start a new thread so that all the clients will be handled simultaneously.
    start_new_thread(threaded_client, (conn, ))
    # threaded_client is a custom function that is used for handling the client for which the thread has been created.
```

### Threaded Function

A thread is just another process that runs in the background along with the main process.

How to create a thread that will handle different clients in the server.

```python
def threaded_client(conn):
    reply = ""
    conn.send(str.encode("Connected"))
    while True:
        try:
            # This is used to define how much and what data are we receiving
            # Here we can receive 2048 bytes of data.
            data = conn.recv(2048)
            # Since the data is encoded, so we need to first decode it to read the information.
            reply = data.decode('utf-8')

            if not data:
                print("Disconnected")
                break
            else:
                print(f"Received: {reply}")
                print(f"Sending: {reply}")
            # Sending the reply to the server.
            conn.sendall(str.encode(reply))
        except:
            break
    print("Lost Connection)
    conn.close()    # For closing the connection to the client
```

Note: For any client to connected the server, the server must be running and only then can the clients connect to eachother via the server.

### Setting the Client

Here using the object oriented approach to create a client so that we don't have to write the code for each client.

In client program also, we use socket module

```python
class Network:
    def __init__(self):
        # The socket specifications need to be the same as in the server.
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # The IP address of the server.
        # Here, since we are running the server and client on the same network, they will have the same IP address.
        self.server = socket.gethostbyname(socket.gethostname())
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            # Sending a connection request to the server
            self.client.connect(self.addr)
            # The server will send the id to the client on the first connection
            return self.client.recv(2048).decode('utf-8')
        except:
            pass

    def send(self, data):
        try:
            # Send data to the server.
            self.client.send(str.encode(data))
            # Send the reply to the client
            return self.client.recv(2048).decode('utf-8')
        except socket.error as e:
            print(e)
```
