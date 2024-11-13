import cv2
import base64
import asyncio
import websockets

websocket_uri = "ws://localhost:8000/start"

async def stream_video():
  async with websockets.connect(websocket_uri) as websocket:
    cap = cv2.VideoCapture(0)
    

    if not cap.isOpened():
      print('Error: Unable to access webcam')
      return

    try:
      while True:
        ret, frame = cap.read()
        if not ret:
            break

        
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            print("Error: Failed to encode the frame.")
            break
        
        frame_bytes = buffer.tobytes()
        frame_base64 = base64.b64encode(frame_bytes).decode('utf-8')

        await websocket.send(frame_base64)

        cv2.imshow("Video Stream", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
          break

    finally:
      cap.release()
      cv2.destroyAllWindows()


if __name__ == '__main__':
  asyncio.run(stream_video())