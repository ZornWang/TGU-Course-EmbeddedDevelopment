import RPi.GPIO as GPIO
import time
import LightController

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
        LightController.some_function()

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

    # def reback(self,flag):
    #     if flag == True:
    #         await self.websocket.send("lightIsOn")
    #     if flag == False:
    #         await self.websocket.send("lightIsOff")