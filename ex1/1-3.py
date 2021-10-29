import thread

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

def led_blink(pin,x):
    while True:
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(x)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(x)

thread.start_new_thread(led_blink,(21,0.5))
thread.start_new_thread(led_blink,(20,1))
thread.start_new_thread(led_blink,(16,1.5))

while 1:
    pass

