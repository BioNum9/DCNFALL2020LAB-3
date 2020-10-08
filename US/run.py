from flask import Flask
from flask import request


app = Flask(__name__)



@app.route('/fibonacci', methods=['GET'])
def process_fibonacci_request():

    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    if not hostname or not fs_port or not number or not as_ip or not as_port:
        # can't get all parameters
        return "Record not found", 400
    

    return 'good', 200

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
