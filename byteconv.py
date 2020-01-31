import struct



#print int('80147113522712023063'.encode('hex'), 16)

#80 14 71 135 227 120 230 63
#"80", "14", "71", "135", "227", "120", "230", "63"
#print struct.calcsize('80147113522712023063')


x = struct.pack('BBBBBBBB', 80, 14, 71, 135, 227, 120, 230, 63)
print x
print struct.unpack('>ii', x)

x = struct.pack('BBBB', 237, 121, 52, 94)
print struct.unpack('@i', x)[0]
