from fastapi import FastAPI
from app.api.v1.user import router

app = FastAPI ()

@app.get ("/")
def road_root():
    return{"hello": "world"}


app.include_router(router)