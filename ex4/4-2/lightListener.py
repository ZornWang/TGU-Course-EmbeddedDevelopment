#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time
import RPi.GPIO as GPIO

class lightListener(threading.Thread):
    def __init__(self, pin):
        threading.Thread.__init__(self)
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    def run(self):
        readLight(self.pin)

def readLight(pin):
    if (GPIO.input(pin) == True):
        return "lightIsOn"
    if (GPIO.input(pin) == False):
        return "lightIsOff"