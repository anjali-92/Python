import zmq
import time
Context = zmq.Context()
socket = Context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(10):
    print("Message sent %s"% request);
    socket.send(b"Hello");

    time.sleep(6)

    message = socket.recv()
    print("Received reply %s "% message)


