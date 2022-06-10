from fastapi import FastAPI
from lib_d.lib_d.foo import foo_helper

app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"Service B using {foo_helper()}"}
