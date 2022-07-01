from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np
from starlette.responses import StreamingResponse
import io

app = FastAPI()

def processImage(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

@app.post("/process")
async def analyze_route(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    img_dimensions = str(img.shape)
    return_img = processImage(img)
    _, im_png = cv2.imencode(".png", return_img)
    streaming_img = StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")
    return streaming_img
