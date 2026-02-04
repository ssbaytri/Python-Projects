from fastapi import FastAPI, HTTPException
from app.schemas import Post
from app.db import Post, create_db, get_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db()
    yield

app = FastAPI(lifespan=lifespan)

