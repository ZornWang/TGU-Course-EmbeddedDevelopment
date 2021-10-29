import asyncio
import websockets
from lightController import *

r_pin = 16
g_pin = 20
b_pin = 21

b_light = Light(b_pin)
g_light = Light(g_pin)
r_light = Light(r_pin)

lights = [r_light,b_light,g_light]

# 接收客户端消息并处理
async def recv_msg(websocket):
    while True:
        recv_text = await websocket.recv()
        recv = recv_text.split(" ")
        command = recv[0]
        num = int(recv[1])-1
        value = recv[2:]
        if command == "turn_on":
            lights[num].turn_on()
        if command == "turn_off":
            lights[num].turn_off()
        if command == "bright":
            lights[num].bright_turn_on(int(value[0]))


# 服务器端主逻辑
async def main_logic(websocket, path):
    await recv_msg(websocket)

start_server = websockets.serve(main_logic, '192.168.10.24', 8080)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

