import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
while True:
    a = 0.16
    for i in range(15):
        for i in range(3):
            GPIO.output(21,GPIO.HIGH)
            time.sleep(a)
            GPIO.output(21,GPIO.LOW)
            time.sleep(a)
        a -= 0.01
    for i in range(15):
        for i in range(3):
            GPIO.output(21, GPIO.HIGH)
            time.sleep(a)
            GPIO.output(21, GPIO.LOW)
            time.sleep(a)
        a += 0.01