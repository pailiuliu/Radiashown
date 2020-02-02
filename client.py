#!python2
# An example script to connect to Google using socket 
# programming in Python 
import socket # for socket 
import sys
import struct
 
az = []
el = []
detCps1 = []
detCps2 = []
detCps3 = []
detCps4 = []
detCps5 = []
detCps6 = []
detCps7 = []
detCps8 = []

detCps = [None] * 8

detectors = [detCps1, detCps2, detCps3, detCps4, detCps5, detCps6, detCps7, detCps8]
 
# Create client socket
try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print "socket successfully created"
except socket.error as err: 
    print "socket creation failed with error %s" %(err)
  
port = 22001
  
try: 
    host_ip = '192.168.1.128'
except socket.gaierror: 
    print "there was an error resolving the host"
    sys.exit() 
  
# Connect to the server 
s.connect((host_ip, port)) 

print "the socket has successfully connected"

byteCount = 1

while (1):
    # Store relevant bytes as an array of integers 
    if byteCount < 138:
        msg = s.recv(1)
        if 38 <= byteCount <= 45: # Store the 8 bytes of the double
            az.append(ord(msg))
        if 46 <= byteCount <= 53:
            el.append(ord(msg))
        if 54 <= byteCount <= 61:
            detCps1.append(ord(msg))
        if 62 <= byteCount <= 69:
            detCps2.append(ord(msg))
        if 70 <= byteCount <= 77:
            detCps3.append(ord(msg))
        if 78 <= byteCount <= 85:
            detCps4.append(ord(msg))
        if 86 <= byteCount <= 93:
            detCps5.append(ord(msg))
        if 94 <= byteCount <= 101:
            detCps6.append(ord(msg))
        if 102 <= byteCount <= 109:
            detCps7.append(ord(msg))
        if 110 <= byteCount <= 117:
            detCps8.append(ord(msg))
                   
        byteCount += 1 
    else:
        # One full msg (137 bytes) has been recieved

        azUni = struct.pack('BBBBBBBB', *az)
        azimuth = struct.unpack('<d', azUni)[0]
    
        elUni = struct.pack('BBBBBBBB', *el)
        elevation = struct.unpack('<d', elUni)[0]

        print "Azimuth = %f\n" % azimuth
        print "Elevation = %f\n" % elevation

        for d in range(0,8):
            thisCps = detectors[d]
            thisCpsUni = struct.pack('BBBBBBBB', *thisCps)
            detCps[d] = struct.unpack('<d', thisCpsUni)[0]
            print "Detector %d Cps = %f\n" % (d, detCps[d])
            
        # Reset the data arrays for next message
        az = []
        el = []
        detCps1 = []
        detCps2 = []
        detCps3 = []
        detCps4 = []
        detCps5 = []
        detCps6 = []
        detCps7 = []
        detCps8 = []

        i = 1

    
