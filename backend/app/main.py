# Ce code permet la création d’un endpoint POST pour recevoir un document via une requête HTTP.

from fastapi import FastAPI 
from pydantic import BaseModel # Pydantic = Bibliothèque qui permet de valider automatiquement les données => permet de définir les modèles de données (ex: les schémas...)

app = FastAPI() 

# ----- Models -----
class Document(BaseModel):
    id:int  
    title:str
    content:str


# ----- Fake DB -----
fake_db = [] 


# ----- Routes -----
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur ton API FastAPI 👋"}
     
@app.post("/documents") # Déclare un endpoint POST à l'URL /document    POST http://localhost:8000/documents (un fichier json sera attendu)
def create_document(doc: Document): 
    fake_db.append(doc) 
    return {"message": "document created", "doc": doc}  

@app.get("/documents")
def get_documents():
    return fake_db

@app.get("/documents/{doc_id}")
def get_documents(doc_id: int):
    for doc in fake_db:
        if doc.id == doc_id:
            return doc
    return {"error": "Document not found"}, 404

@app.delete("/documents/{doc_id}")
def delete_documents(doc_id: int):
    for doc in fake_db:
        if doc.id == doc_id:
            fake_db.remove(doc)
            return {"message": "Document deleted"}
    return {"error": "Document not found"}, 404