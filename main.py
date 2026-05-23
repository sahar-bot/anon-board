from typing import Annotated
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from schemas import SMessageAdd, SMessageGet
from router import router as messages_router




@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Database is cleared")
    await create_tables()
    print("Database is ready")
    yield
    print("Turning off")

app = FastAPI(lifespan=lifespan)
app.include_router(messages_router)






