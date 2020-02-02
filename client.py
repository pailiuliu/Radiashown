#!python2
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

i = 1

while (1):
    if i < 138:
        msg = s.recv(1)
        if 38 <= i <= 45:
            az.append(ord(msg))
        if 46 <= i <= 53:
            el.append(ord(msg))
        if 54 <= i <= 61:
            detCps1.append(ord(msg))
        if 62 <= i <= 69:
            detCps2.append(ord(msg))
        if 70 <= i <= 77:
            detCps3.append(ord(msg))
        if 78 <= i <= 85:
            detCps4.append(ord(msg))
        if 86 <= i <= 93:
            detCps5.append(ord(msg))
        if 94 <= i <= 101:
            detCps6.append(ord(msg))
        if 102 <= i <= 109:
            detCps7.append(ord(msg))
        if 110 <= i <= 117:
            detCps8.append(ord(msg))
                   
        i += 1
    else:
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

    
