import RPi.GPIO as GPIO
import time
from flask import request
from flask import Flask
from flask import render_template
from flask_socketio import SocketIO,send

app = Flask(__name__,static_url_path='',template_folder='./template')
socketio = SocketIO(app)

class Light:
    def __init__(self, pin):
        self.__pin = pin
        self.__pwm = None
        self.flag = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    def __del__(self):
        print(self.__class__.__name__, 'del')
        self.turn_off()

    def addWebsocket(self,websocket):
        self.websocket = websocket

    def turn_on(self):
        GPIO.output(self.__pin, GPIO.HIGH)
        some_function()

    def turn_off(self):
        GPIO.output(self.__pin, GPIO.LOW)

    def blink(self):
        frequency, times = 5,5
        for i in range(int(times)):
            for i in range(int(frequency)):
                GPIO.output(self.__pin, GPIO.HIGH)
                time.sleep(1.0 / (frequency * 2))
                GPIO.output(self.__pin, GPIO.LOW)
                time.sleep(1.0 / (frequency * 2))

r_pin = 16
g_pin = 20
b_pin = 21

b_light = Light(b_pin)
g_light = Light(g_pin)
r_light = Light(r_pin)
lights = {'red':r_light,'blue':b_light,'green':g_light}


@app.route('/')
def index():
    return render_template('client.html')

@app.route('/lightControl')
def lightControl():
    # some_function()
    return lightService(command=request.args.get('command'))

def some_function():
    socketio.emit('some event', {'data': 42})

def lightService(command):
    if command == 'light_on':
        lights['blue'].turn_on()
        return 'light is on'
    if command == 'light_off':
        lights['blue'].turn_off()
        return 'light is off'
    if command == 'blink':
        lights['blue'].blink()
        return 'light is blinking'

if __name__ == '__main__':
    socketio.run(app, host='192.168.10.24', port=5000, debug=True)
