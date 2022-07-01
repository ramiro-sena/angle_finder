from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np
from starlette.responses import StreamingResponse
import io
import time

app = FastAPI()

def processImage(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

@app.get("/", tags=["Root"])
async def read_root():
  return { 
    "message": "Welcome to my notes application, use the /docs route to proceed"
   }

@app.post("/process")
async def analyze_route(file: UploadFile = File(...)):
    contents = await file.read()
    print(f'read = {time.time()}')
    nparr = np.fromstring(contents, np.uint8)
    print(f'to array = {time.time()}')
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    print(f'decode = {time.time()}')
    return_img = processImage(img)
    _, im_png = cv2.imencode(".png", return_img)
    streaming_img = StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")
    print(f'streaming = {time.time()}')
    return streaming_img
