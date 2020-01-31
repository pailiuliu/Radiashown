import struct

#Time
x = struct.pack('BBBB', 237, 121, 52, 94)
print struct.unpack('i', x)[0]

#Azimuth
x = struct.pack('BBBBBBBB', 80, 14, 71, 135, 227, 120, 230, 63)
print struct.unpack('<d', x)[0]

