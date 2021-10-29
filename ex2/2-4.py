import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
f = open("config2.txt")
a = f.readlines()

def blink(frequency,times):
    for i in range(int(times)):
        for i in range(int(frequency)):
            GPIO.output(21,GPIO.HIGH)
            time.sleep(1.0/(frequency*2))
            GPIO.output(21, GPIO.LOW)
            time.sleep(1.0/(frequency*2))

def ledOn(times):
    GPIO.output(21,GPIO.HIGH)
    time.sleep(times)
    GPIO.output(21,GPIO.LOW)

for i in range(len(a)):
    str = a[i]
    str_split = str.split(",")
    if str_split[0] == "blink":
        blink(int(str_split[1]),int(str_split[2]))
    if str_split[0] == "led-on":
        ledOn(int(str_split[1]))
    time.sleep(1)

