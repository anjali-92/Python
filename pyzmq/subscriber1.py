import zmq
import sys
import time

Context = zmq.Context()
socket = Context.socket(zmq.SUB)

print len(sys.argv)
port = sys.argv[1]
print port
socket.connect("tcp://localhost:%s"% port)

port1 = sys.argv[2]
print port1
socket.connect("tcp://localhost:%s"% port1)
'''
port = 5999
if len(sys.argv) == 2:
    port = sys.argv[1]
    print port
    socket.connect("tcp://localhost:%s"% port)

if len(sys.argv) == 3:
    port1 = sys.argv[2]
    print port1
    socket.connect("tcp://localhost:%s"% port)
'''
topic1 = "Lesson for Life"
topic2 = "Remember"

socket.setsockopt( zmq.SUBSCRIBE, topic1 )

while True:
    data = socket.recv()
    print data
    topic,message = data.split(',')
    print("Topic   %s \n Message    %s"% (topic, message))
    time.sleep(1)

