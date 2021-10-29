import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pin_led = 21
GPIO.setup(pin_led,GPIO.OUT)

def lightController(data):
    if data.find("light on", 0, len(data)) == 0:
        GPIO.output(pin_led, GPIO.HIGH)
    if data.find("light off", 0, len(data)) == 0:
        GPIO.output(pin_led, GPIO.LOW)

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