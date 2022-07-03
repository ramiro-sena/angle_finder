from fastapi import FastAPI, UploadFile, File
import numpy as np
import cv2
import time
app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Server is up and running!"}

@app.get("/getTime")
def getTime():
    return {"message": f"{time.time()}"}

@app.post("/analyze")
async def analyze_route(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    img_dimensions = str(img.shape)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # line that fixed it
    _, encoded_img = cv2.imencode('.PNG', gray)

    encoded_img = base64.b64encode(encoded_img)

    return{
        'filename': file.filename,
        'dimensions': img_dimensions,
        'encoded_img': endcoded_img,
    }