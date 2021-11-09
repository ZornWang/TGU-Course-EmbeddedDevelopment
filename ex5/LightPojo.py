import RPi.GPIO as GPIO
import time

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

    async def turn_on(self):
        GPIO.output(self.__pin, GPIO.HIGH)
        await self.reback(True)

    async def turn_off(self):
        GPIO.output(self.__pin, GPIO.LOW)
        await self.reback(False)

    async def blink(self):
        frequency, times = 5,5
        for i in range(int(times)):
            for i in range(int(frequency)):
                GPIO.output(self.__pin, GPIO.HIGH)
                await self.reback(True)
                time.sleep(1.0 / (frequency * 2))
                GPIO.output(self.__pin, GPIO.LOW)
                await self.reback(False)
                time.sleep(1.0 / (frequency * 2))

    async def reback(self,flag):
        if flag == True:
            await self.websocket.send("lightIsOn")
        if flag == False:
            await self.websocket.send("lightIsOff")