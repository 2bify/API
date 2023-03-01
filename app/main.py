
from fastapi import FastAPI, Response, HTTPException,Depends
#from fastapi.params import Body
from . import models
from .database import engine
from .routers import user, post , auth ,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
#models.Base.metadata.create_all(bind=engine)

app=FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message":"Welcome to the API"}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
