import json
import socket

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

# /fibonacci?hostname=fibonacci.com&fs_port=K&number=X&as_ip=Y&as_port=Z

@app.route('/register', methods=['PUT'])
def process_register_request():

    data = request.get_data()
    dict1 = json.loads(data)
    hostname = dict1['hostname']
    ip       = dict1['ip']
    as_ip    = dict1['as_ip']
    as_port  = dict1['as_port']

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # send_addr = (as_ip, 53533)

    send_data = {}
    send_data['TYPE'] = 'A'
    send_data['NAME'] = 'fibonacci.com'
    send_data['VALUE'] = ip
    send_data['TTL'] = 10
    
    json_data = json.dumps(send_data)

    udp_socket.sendto(json_data, (as_ip, as_port))



    return "Record not found", 400
    
@app.route('/fibonacci', methods=['GET'])
def process_fibonacci_request():
    
    number = request.args.get('number')

    if isinstance(number, int):
        
        return "Bad format", 400

    fibo_list = []
    if number <= 0:
        return fibo_list
    else:
        x, y = 0, 1
        for i in range(number):
            fibo_list.append(y)
            x, y = y, x + y


    return fibo_list, 200


app.run(host='0.0.0.0',
        port=9090,
        debug=True)
