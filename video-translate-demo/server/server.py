from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uuid
import uvicorn
import asyncio

app = FastAPI()


active_streams = {}


@app.get("/")
async def get_available_streams():
  return {"streams": list(active_streams.keys())}



@app.websocket('/start')
async def start_stream(websocket: WebSocket):
  await websocket.accept()

  stream_id = str(uuid.uuid4())

  active_streams[stream_id] = None

  try:
    while True:
      data = await websocket.receive_text()
      active_streams[stream_id] = data
      print(data)
  finally:
    del active_streams[stream_id]


@app.websocket('/connect/{stream_id}')
async def connect_to_stream(websocket: WebSocket, stream_id: str):
  await websocket.accept()

  try:
    while True:
      cap = active_streams[stream_id]

      await websocket.send_text(cap)
      await asyncio.sleep(0.03)

  finally:
    del active_streams[stream_id]


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000)

