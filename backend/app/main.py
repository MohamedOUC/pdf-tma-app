from fastapi import FastAPI
from .database import engine, Base
from .routes import documents

app = FastAPI() 

Base.metadata.create_all(bind=engine)

app.include_router(documents.router, tags=["Documents"])