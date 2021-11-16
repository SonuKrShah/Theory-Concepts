Here we will use pickle for transmitting the data from the client to the server.

Also we will be using pygame module for building the graphical user interface.

Basically, we will have two clients represented by rectangles and then if we move the client on the home terminal then it moves on the other client's terminal as well.

### Client

For the client, we will use the object oriented programming for setting up the client and connecting to the server.

Here, the client will send it's position to the server and then the server will update that position on it's side and then return the current position of the other player.

```python
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.PORT = 5555
        self.ADDR = (self.SERVER, self.PORT)
        self.pos = self.connect()

    def get_pos(self):
        return self.get_pos

    def connect(self):
        try:
            self.client.connect(self.ADDR)
            # Here the server will be sending the current position of the opponent.
            return self.client.recv(2048).decode('utf-8')
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode('utf-8')
        except socket.error as e:
            print(e)
```
