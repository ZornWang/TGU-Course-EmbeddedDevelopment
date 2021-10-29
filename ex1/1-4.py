import time

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(18,GPIO.IN,GPIO.PUD_UP)
GPIO.output(21,GPIO.LOW)
flag = True
changeTime = 0

while True:
    time.sleep(0.3)
    if GPIO.input(18) == 0:
        flag = not flag
        GPIO.output(21, GPIO.LOW if flag else GPIO.HIGH)