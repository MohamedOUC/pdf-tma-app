from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Chargement des variables d'environnement depuis .env
load_dotenv()

# URL de connexion à la base PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")

# Moteur de base de données
engine = create_engine(DATABASE_URL)

# Session = onject qui permet de faire des requêtes SQL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = classe mère qui permet de faire des requêtes SQL
Base = declarative_base()

# get_db = fonction à importer dans mon backend/app/database.py
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()