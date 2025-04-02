from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from .. import models, schemas, database
from typing import Optional
import os
import shutil


router = APIRouter()
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Créer un document
@router.post("/documents/", response_model=schemas.Document)
def create_document(doc: schemas.DocumentCreate, db: Session = Depends(get_db)):
    print("Document reçu :", doc)
    db_doc = models.Document(**doc.dict())
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)
    return db_doc

# Récupéré un document
@router.get("/documents/", response_model=list[schemas.Document])
def get_documents(db: Session = Depends(database.get_db)):
    return db.query(models.Document).all()

# Rechercher des documents par titre (ilike)
@router.get("/documents/search", response_model=list[schemas.Document])
def search_documents(title: str, db: Session = Depends(get_db)):
    return db.query(models.Document).filter(models.Document.title.ilike(f"%{title}%")).all()

# Supprimer un document par ID
@router.delete("/documents/{doc_id}")
def delete_document(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(models.Document).filter(models.Document.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document non trouvé")
    db.delete(doc)
    db.commit()
    return {"message": "Document supprimé"}

# Mettre à jour un document existant
@router.put("/documents/{doc_id}", response_model=schemas.Document)
def update_document(doc_id: int, update: schemas.DocumentCreate, db: Session = Depends(get_db)):
    doc = db.query(models.Document).filter(models.Document.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document non trouvé")
    doc.title = update.title
    doc.content = update.content
    db.commit()
    db.refresh(doc)
    return doc

# Route pour upload des fichiers
@router.post("/documents/uploads", response_model=schemas.Document)
async def upload_document(
    title: str = Form(...),
    content: str = Form(...),
    file: Optional[UploadFile] = File(None), # Facultatif
    db: Session = Depends(get_db)
):
    file_path = None
    
    if file:
        UPLOAD_DIR = "uploads"
        if not os.path.exists(UPLOAD_DIR):
            os.makedirs(UPLOAD_DIR)
        file_path = f"{UPLOAD_DIR}/{file.filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
    doc = models.Document(title=title, content=content, file_path=file_path)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc