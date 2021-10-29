import RPi.GPIO as GPIO
import websocket
import json
import threading
import time

R = 16
G = 20
B = 21

def socket_client():
    # 创建 WebSocket 客户端连接服务器，并发送消息告知服务器准备就绪
    ws = websocket.create_connection("ws://192.168.10.15:9511")
    req = {"terminal": "smart_car"}
    ws.send(json.dumps(req))
    # 监听来自服务器的消息
    while True:
        res = ws.recv()
        res = json.loads(res)
        if res.__contains__('action') and res.__contains__('err_code') and res['err_code'] == 0:
            global action
            action = res['action']
            # 开灯
            if res['action'] == 'light_on':
                lightOn()
            # 关灯
            if res['action'] == 'light_off':
                lightOff()
        else:
            print('error')

def lightOn():
    GPIO.output(R, GPIO.HIGH)

def lightOff():
    GPIO.output(R, GPIO.LOW)

# 多线程执行 线程启动时连接服务器
class EventThread(threading.Thread):
    def run(self):
        socket_client()

# 初始化树莓派引脚
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(R, GPIO.OUT)
    GPIO.setup(G, GPIO.OUT)
    GPIO.setup(B, GPIO.OUT)

#   初始化引脚
init()

# 启动线程监听服务端消息
eventThread = EventThread()
eventThread.start()
