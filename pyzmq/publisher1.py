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
pub1_socket = Context.socket(zmq.PUB)
pub2_socket = Context.socket(zmq.PUB)

print len(sys.argv)
try:
    port = sys.argv[1]
    print port
    pub1_socket.bind("tcp://*:%s"% port)

    port1 = sys.argv[2]
    print port1
    pub2_socket.bind("tcp://*:%s"% port1)
except Exception, e:
    print e

topic1 = "Lesson for Life"
message_data1 = "from PUB1: Keep Improving."

topic2 = "Remember"
message_data2 = "from PUB2: Your Body is never tired."

flag = 0
try:
    while True:
	if flag == 0:
	    pub1_socket.send( "%s , %s"% (topic1, message_data1) )
	    flag = 1
	elif flag == 1:
	    pub2_socket.send( "%s , %s"% (topic1, message_data2) )
	    flag = 0
	time.sleep(1)
except Exception, e:
    print e
    print "Exception caught"
finally:
    print "\nExiting Application"

