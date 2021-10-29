import socket
import RPi.GPIO as GPIO
import time\

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pin_led = 21
GPIO.setup(pin_led,GPIO.OUT)

def lightController(data):
    split = data.split(",")
    if split is None:
        split = data.split(" ")
    if data.find("light on", 0, len(data)) == 0:
        GPIO.output(pin_led, GPIO.HIGH)
    if data.find("light off", 0, len(data)) == 0:
        GPIO.output(pin_led, GPIO.LOW)
    if data.find("blink", 0, len(data)) == 0:
        blink(int(split[1]),int(split[2]))


def blink(frequency,times):
    for i in range(int(times)):
        for i in range(int(frequency)):
            GPIO.output(21,GPIO.HIGH)
            time.sleep(1.0/(frequency*2))
            GPIO.output(21, GPIO.LOW)
            time.sleep(1.0/(frequency*2))

address = ('192.168.10.24', 5005)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(5)
conn, addr = s.accept()
print('[+] Connected with', addr)
while True:
    data = conn.recv(1024)
    data = data.decode()
    if data is None:
        continue
    if data == "exit":
        break
    lightController(data)
conn.close()
s.close()