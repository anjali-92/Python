import zmq
import time


def message_producer():
    Context = zmq.Context()
    socket = Context.socket(zmq.PUSH)
    socket.bind("tcp://127.0.0.1:5678")

    for i in range(1000):
	json_data = { 'num' : i }
	socket.send_json( json_data )
	time.sleep(1)

message_producer()
