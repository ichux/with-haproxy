import asyncio
import json

import websockets
from lights import calculate_idle


async def calculate_idle(t, conn_open_event):
    orig_time = t
    while True:
        await conn_open_event.wait()
        print("Connection is now open from idle")


async def init_connection(message, conn_open_event):
    # Get global variable to set
    global CLIENT_WS
    uri = WS_URI
    async with websockets.connect(uri) as websocket:
        print("Connection is open from socket")
        conn_open_event.set()
        CLIENT_WS = websocket
        CONNECTION_OPEN = True
        # send init message
        await websocket.send(message)
        while CONNECTION_OPEN:
            await handleMessages(websocket, message)
        await websocket.send(
            json.dumps({"type": MessageType.Close.name, "message": USERNAME})
        )
        await websocket.close()


async def main():
    message = json.dumps({"payload": "payload"})
    loop = asyncio.get_event_loop()
    event = asyncio.Event()
    start_light = asyncio.create_task(calculate_idle(3, event))
    await asyncio.gather(init_connection(message, event), start_light)


asyncio.run(main())
