import json
import socket
import redis
from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)




# r = redis.Redis(host='localhost', port=6379, decode_responses=True)   # set redis


def dns_server():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind('127.0.0.1',53533)
    while True:
        data, addr = udp_socket.recvfrom(8192)
    
def send_info():
    #r.set('hostname', 'fiboccino')   
    
    
app.run(host='0.0.0.0',
        port=9091,
        debug=True)
