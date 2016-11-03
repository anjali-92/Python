import zmq
import time
import random

def message_consumer():
    Context = zmq.Context()
    
    message_consumer_recv = Context.socket(zmq.PULL)
    message_consumer_recv.connect("tcp://127.0.0.1:5678")

    message_consumer_send = Context.socket(zmq.PUSH)
    message_consumer_send.connect("tcp://127.0.0.1:5679")

    consumer_id = random.randrange(1,1000)
    while True:
       	work = message_consumer_recv.recv_json()
	data = work['num']
	result = { 'consumer' : consumer_id , 'num' : data }
	if data%2 == 0:
	    message_consumer_send.send_json(result)


message_consumer()


	

    

