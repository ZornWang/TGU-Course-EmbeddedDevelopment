import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(21, GPIO.OUT)

last = 0

while True:
    if GPIO.input(18) == 0:
        if time.time() - last < 0.7:
          GPIO.output(21,GPIO.LOW)
        else:
          GPIO.output(21,GPIO.HIGH)
        time.sleep(0.5)
        last = time.time()
