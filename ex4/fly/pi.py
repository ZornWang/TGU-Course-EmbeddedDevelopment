import logging
from RPi import GPIO
import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

R, G, B = 16, 20, 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)

pwmR = GPIO.PWM(R, 50)
pwmG = GPIO.PWM(G, 50)
pwmB = GPIO.PWM(B, 50)

pwmR.start(0)
pwmG.start(0)
pwmB.start(0)


@sio.event
def color(sid, data):
    logging.info(data)
    pwmR.ChangeDutyCycle(data['r'] / 255 * 100)
    pwmG.ChangeDutyCycle(data['g'] / 255 * 100)
    pwmB.ChangeDutyCycle(data['b'] / 255 * 100)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.info('service start')
    eventlet.wsgi.server(eventlet.listen(('', 10268)), app)