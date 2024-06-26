from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables, delete_tables
from router import tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    print("BASE READY")
    yield
    print("EXIT")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)