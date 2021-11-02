import asyncio
import websockets
from lightController import *

r_pin = 16
g_pin = 20
b_pin = 21

b_light = Light(b_pin)
g_light = Light(g_pin)
r_light = Light(r_pin)

# 接收客户端消息并处理
async def recv_msg(websocket):
    while True:
        recv_text = await websocket.recv()
        print(recv_text)
        if recv_text == "light_on":
            await r_light.turn_on(websocket)
        if recv_text == "light_off":
            await r_light.turn_off(websocket)
        if recv_text == "blink":
            await r_light.blink(websocket)

# 服务器端主逻辑
async def main_logic(websocket, path):
    await recv_msg(websocket)

start_server = websockets.serve(main_logic, '192.168.10.24', 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()