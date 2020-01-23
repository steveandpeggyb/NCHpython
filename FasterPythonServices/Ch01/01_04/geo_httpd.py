"""Geo HTTP server"""
import math
from flask import Flask, request, jsonify

app = Flask(__name__)


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


@app.route('/dist', methods=['POST'])
def dist():
    """Distance API endpoint"""
    src, dest = request.json['src'], request.json['dest']
    dist = haversine(src['lat'], src['lng'], dest['lat'], dest['lng'])
    return jsonify(ok=True, unit='km', distance=dist)


if __name__ == '__main__':
    app.run(port=8080)
