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
az = []
el = []
i = 1

while (1):
    if i < 138:
        msg = s.recv(1)
        if 38 <= i <= 45:
            az.append(ord(msg))
        if 46 <= i <= 53:
            el.append(ord(msg))
            
        i += 1
    else:
        azUni = struct.pack('BBBBBBBB', *az)
        azimuth = struct.unpack('<d', azUni)[0]
    
        elUni = struct.pack('BBBBBBBB', *el)
        elevation = struct.unpack('<d', elUni)[0]

        print "Azimuth = %f\n" % azimuth
        print "Elevation = %f\n" % elevation
        az = []
        el = []
        i = 1

    
