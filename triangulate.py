#!python2
# An example script to connect to Google using socket 
# programming in Python 
import socket # for socket 
import sys
import struct

radAssistPort = 22001

checkCps = False;
currentX = 10
currentY = 2
angle = 90

sampleList = []
numSamples = 0 #total number of samples
tCount = 0 #number of samples that have been triangulated
radiationMap = {}

#used to dislay the radiation icon on screen
maxReading = 0
maxCoordinates = []

class Sample:
    def __init__(self, x, y, angle, az, el, avgCps):
        self.x = x
        self.y = y
        self.angle = angle
        self.az = az
        self.el = el
        self.avgCps = avgCps
        
        self.theta = self.angle + self.az
        self.slope = math.tan(self.theta)

        #compare to maxReading 
        if self.avgCps > maxReading:
            maxReading = self.avgCps
            maxCoordinates = [self.x, self.y]

def getRadAssistData(port, x, y, angle):
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
    thisCps = []

    detCps = [None] * 8

    detectors = [detCps1, detCps2, detCps3, detCps4, detCps5, detCps6, detCps7, detCps8]
     
    byteCount = 1

    # Store relevant bytes as an array of integers 
    if byteCount < 138:
        msg = s.recv(1)
        if 38 <= byteCount <= 45: # Store the 8 bytes of the double
            az.append(ord(msg))
        else if 46 <= byteCount <= 53:
            el.append(ord(msg))
        else if 54 <= byteCount <= 61:
            detCps1.append(ord(msg))
        else if 62 <= byteCount <= 69:
            detCps2.append(ord(msg))
        else if 70 <= byteCount <= 77:
            detCps3.append(ord(msg))
        else if 78 <= byteCount <= 85:
            detCps4.append(ord(msg))
        else if 86 <= byteCount <= 93:
            detCps5.append(ord(msg))
        else if 94 <= byteCount <= 101:
            detCps6.append(ord(msg))
        else if 102 <= byteCount <= 109:
            detCps7.append(ord(msg))
        else if 110 <= byteCount <= 117:
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

        detectors = [detCps1, detCps2, detCps3, detCps4, detCps5, detCps6, detCps7, detCps8]

        for d in range(0,8):
            thisCps = detectors[d]
            thisCpsUni = struct.pack('BBBBBBBB', *thisCps)
            detCps[d] = struct.unpack('<d', thisCpsUni)[0]
            print "Detector %d Cps = %f\n" % (d+1, detCps[d])

        #calculate average cps value
        for i in range(0,8);
            totalCps += detCps[i]
        avgCps = totalCps/8

        return avgCps
            
    #create an instance of Sample class
    sampleList.append(Sample(x, y, angle, azimuth, elevation, avgCps))
    numSamples += 1
    #radiation check completed, reset flag
    checkRadiation = False

def triangulate(s1, s2):
    estimateX = ((s2.slope * s2.x) - (s1.slope * s1.x) + s1.y - s2.y) / (s2.slope - s1.slope)
    estimateY = s1.slope * (estimateX - s1.x) + s1.y

    return estimateX, estimateY


def main():
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

    while True:
        while checkCps is True:
            getRadAssistData(radAssistPort, currentX, currentY, currentAngle)
        if tCount = numSamples - 1:
            for i in range(0,tCount):
                triangulate(sampleList[i],sampleList[tCount])
        else if tCount < numSamples - 1:
            print "Error: missed the triangulation of sample"
        else:
            print "Error: did extra triangulation"
            
	
if __name__ == '__main__':
    main()
    
