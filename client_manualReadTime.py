# An example script to connect to Google using socket 
# programming in Python 
import socket # for socket 
import sys  
  
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
timeInts = []
timeBits = ''

i = 1
while i <= 137:
    msg = s.recv(1)
    if i > 9 and i < 14:
        print i
        timeInts.insert(0,ord(msg))
    i = i + 1

for b in range(0,4):
    timeBits += bin(timeInts[b])[2:].zfill(8)
    b +=1
    
print >> sys.stderr,'timeBits = %s\n' % timeBits

unix_time = int(timeBits, 2)
print >> sys.stderr, 'unix timestamp = %s\n' % unix_time

print 'Check:'
import time

print time.time()
    
