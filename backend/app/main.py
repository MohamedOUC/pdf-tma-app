from fastapi import FastAPI
from .database import engine, Base
from .routes import documents
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() 

Base.metadata.create_all(bind=engine)

app.include_router(documents.router, tags=["Documents"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)