"""Geo TCP server"""
import math
import struct


def haversine(lat1, lng1, lat2, lng2):
    """Compute the distable in km between two points"""
    phi1 = math.radians(90 - lat1)
    phi2 = math.radians(90 - lat2)

    theta1 = math.radians(lng1)
    theta2 = math.radians(lng2)

    cos = (math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2) +
           math.cos(phi1) * math.cos(phi2))
    arc = math.acos(cos)
    return arc * 6373  # Earth radius in km


if __name__ == '__main__':
    import zmq

    ctx = zmq.Context()
    sock = ctx.socket(zmq.REP)
    sock.bind('tcp://*:7000')

    while True:
        msg = sock.recv()
        try:
            lat1, lng1, lat2, lng2 = struct.unpack('>dddd', msg)
            dist = haversine(lat1, lng1, lat2, lng2)
        except struct.error:
            dist = -1

        out = struct.pack('>d', dist)
        sock.send(out)
