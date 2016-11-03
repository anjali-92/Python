'''
Client[REQ//REQUEST] / Server[REP//RESPONSE]
Request/Reply pattern

Most basic pattern is client/server model, where client sends a request and server replies to the request.

There is one difference from zmq.PAIR and other type of ZMQ sockets.

ZMQ REQ sockets can connect to many servers.
The requests will be interleaved or distributed to both the servers.
With socket zmq.PAIR, you could send any number of messages among connected peers or client/server.

socket zmq.REQ will block on send unless it has successfully received a reply back.
socket zmq.REP will block on recv unless it has received a request.
Each Request/Reply is paired and has to be successful.

'''
import zmq
import time

Context = zmq.Context()
socket = Context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    print("Message received %s"% message)

    time.sleep(1)

    socket.send(b"World")

