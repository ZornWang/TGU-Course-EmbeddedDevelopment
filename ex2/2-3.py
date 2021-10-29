import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
f = open("config.txt")
a = f.readlines()
for i in range(len(a)):
    for j in range(int(a[i])):
        GPIO.output(21,GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(21,GPIO.LOW)
        time.sleep(0.3)
    time.sleep(1)