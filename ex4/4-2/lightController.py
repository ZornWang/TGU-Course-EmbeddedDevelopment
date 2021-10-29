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

    async def turn_on(self, websocket):
        GPIO.output(self.__pin, GPIO.HIGH)
        await self.reback(True,websocket)

    async def turn_off(self, websocket):
        GPIO.output(self.__pin, GPIO.LOW)
        await self.reback(False, websocket)

    async def blink(self, websocket):
        frequency, times = 5,5
        for i in range(int(times)):
            for i in range(int(frequency)):
                GPIO.output(self.__pin, GPIO.HIGH)
                await self.reback(True, websocket)
                time.sleep(1.0 / (frequency * 2))
                GPIO.output(self.__pin, GPIO.LOW)
                await self.reback(False, websocket)
                time.sleep(1.0 / (frequency * 2))

    @staticmethod
    async def reback(flag, websocket):
        if flag == True:
            await websocket.send("lightIsOn")
        if flag == False:
            await websocket.send("lightIsOff")