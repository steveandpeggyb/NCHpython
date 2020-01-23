"""Geo TCP client"""
import struct
import zmq


ctx = zmq.Context()
sock = ctx.socket(zmq.REQ)
sock.connect('tcp://localhost:7000')

lat1, lng1 = 34.3852712, -119.487444  # Recording booth
lat2, lng2 = 37.7765072, -122.3942272  # Dropbox HQ (where Guido works)

msg = struct.pack('>dddd', lat1, lng1, lat2, lng2)
sock.send(msg)
data = sock.recv()
dist, = struct.unpack('>d', data)
print('distance = {:.2f}'.format(dist))


#Benchmark
from time import monotonic

start = monotonic()
count = 100_000
for i in range (count):
    msg = struct.pack('>dddd', lat1, lng1, lat2, lng2)
    sock.send(msg)
    data = sock.recv()
    dist, = struct.unpack('>d', data)

duration = monotonic() - start
print('{:.2f} RPS'.format(count/duration))