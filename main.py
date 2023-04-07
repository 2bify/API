from fastapi import FastAPI
from routers import predict, search, add_data, total
import models
from database import engine
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app=FastAPI()
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"message":"Server running on -> http://localhost/8000"}

app.include_router(search.router)
app.include_router(predict.router)
app.include_router(add_data.router)
app.include_router(total.router)
