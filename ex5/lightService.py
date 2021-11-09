import asyncio
import websockets
from Light import *

r_pin = 16
g_pin = 20
b_pin = 21

b_light = Light(b_pin)
g_light = Light(g_pin)
r_light = Light(r_pin)
lights = {'red':r_light,'blue':b_light,'green':g_light}

def lightService(command):
    if command == 'light_on':
        lights['blue'].turn_on()
        return 'light is on'
    if command == 'light_off':
        lights['blue'].turn_off()
        return 'light is off'
    if command == 'blink':
        lights['blue'].blink()
        return 'light is blinking'


# 接收客户端消息并处理
# async def recv_msg(websocket):
#     while True:
#         recv_text = await websocket.recv()
#         print(recv_text)
#         if recv_text == "light_on":
#             await lights['red'].turn_on()
#         if recv_text == "light_off":
#             await lights['red'].turn_off()
#         if recv_text == "blink":
#             await lights['red'].blink()

# # 服务器端主逻辑
# async def main_logic(websocket, path):
#     # lights['red'].addWebsocket(websocket)
#     # lights['blue'].addWebsocket(websocket)
#     # lights['green'].addWebsocket(websocket)
#     await recv_msg(websocket)
#
# def websocketInit():
#     start_server = websockets.serve(main_logic, '192.168.10.24', 5678)
#     asyncio.get_event_loop().run_until_complete(start_server)
#     asyncio.get_event_loop().run_forever()