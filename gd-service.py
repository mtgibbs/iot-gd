import logging
import json
import time

from logging.handlers import RotatingFileHandler
from flask import Flask
from grovepi import *

GARAGE_DOOR_READER_RANGE = 30

app = Flask(__name__)

relay = 5;
ultrasonic_ranger = 6;
pinMode(relay, 'OUTPUT')

@app.route('/status')
def status():
    return json.dumps({}, 200, {'ContentType':'application/json'})

@app.route('/readRanger')
def readRanger():
    read = ultrasonicRead(ultrasonic_ranger)
    return 'ultrasonic reader read: {}'.format(read)

@app.route('/up')
def up():
    try:
        if (not is_door_up()):
            activate_relay_switch()
        return json.dumps({'Success': not is_door_up()}, 200, {'ContentType':'application/json'})
    except Exception as ex:
        app.logger.error(ex)
        return json.dumps({'Success': false}, 500, {'ContentType':'application/json'})

@app.route('/down')
def down():
    try:
        if (is_door_up()):
            activate_relay_switch()
        return json.dumps({'Success': is_door_up()}, 200, {'ContentType':'application/json'})
    except Exception as ex:
        app.logger.error(ex)
        return json.dumps({'Success': false}, 500, {'ContentType':'application/json'})
    
def is_door_up():
    return ultrasonicRead(ultrasonic_ranger) < GARAGE_DOOR_READER_RANGE

def activate_relay_switch():
    app.logger.info('Relay switch activated')
    digitalWrite(relay, 1)
    time.sleep(1)
    digitalWrite(relay, 0)


if __name__ == '__main__':
    handler = RotatingFileHandler('iot-gd.log')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.run(host='0.0.0.0', port=80, debug=True)
    app.logger.info('App started.')