# An example script to connect to Google using socket 
# programming in Python 
import socket # for socket 
import sys
import struct
  
try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print "Socket successfully created"
except socket.error as err: 
    print "socket creation failed with error %s" %(err)
  
# default port for socket 
port = 22001
  
try: 
    host_ip = '192.168.1.128'
except socket.gaierror: 
  
    # this means could not resolve the host 
    print "there was an error resolving the host"
    sys.exit() 
  
# connecting to the server 
s.connect((host_ip, port)) 

print "the socket has successfully connected"
time = []
timeBits = ''

i = 1
while i <= 137:
    msg = s.recv(1)
    if i > 9 and i < 14:
        time.append(ord(msg))
    i = i + 1

x = struct.pack('BBBB', *time)
print struct.unpack('<i', x)[0]

print 'Check:'
import time

print time.time()
    
