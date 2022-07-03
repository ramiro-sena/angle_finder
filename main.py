from fastapi import FastAPI
import time
app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Server is up and running!"}

@app.get("/getTime")
def getTime():
    return {"message": f"{time.time()}"}