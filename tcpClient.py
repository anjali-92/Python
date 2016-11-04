# Echo client program
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50011         # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
s.sendall('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)

print "SECOND CONNECTION"

st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
st.connect((HOST, PORT))
st.sendall('Hello, world')
data = st.recv(1024)
st.close()
print 'Received in st', repr(data)
