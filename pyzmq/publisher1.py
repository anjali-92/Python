'''
Multiple publisher and single subscriber

How to call
python publisher1.py 5678 6789
python subscriber1.py 5678 6789

'''
import zmq
import sys
import time
#So that we can start two publisher on different ports

# context maintains a separate thread and state for zmq
Context = zmq.Context()
socket = Context.socket(zmq.PUB)
socket1 = Context.socket(zmq.PUB)

print len(sys.argv)
port = sys.argv[1]
print port
socket.bind("tcp://*:%s"% port)

port1 = sys.argv[2]
print port1
socket1.bind("tcp://*:%s"% port1)

topic1 = "Lesson for Life"
message_data1 = "from PUB1: Keep Improving."

topic2 = "Remember"
message_data2 = "from PUB2: Your Body is never tired."

flag = 0
try:
    while True:
	if flag == 0:
	    socket.send( "%s , %s"% (topic1, message_data1) )
	    flag = 1
	elif flag == 1:
	    socket1.send( "%s , %s"% (topic1, message_data2) )
	    flag = 0
	time.sleep(1)
except Exception, e:
    print e
    print "Exception caught"
finally:
    print "\nExiting Application"

