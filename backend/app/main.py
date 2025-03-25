# Ce code permet la création d’un endpoint POST pour recevoir un document via une requête HTTP.

from fastapi import FastAPI # Import de FastAPI pour créer une appli web/API
from pydantic import BaseModel # Pydantic = Bibliothèque qui permet de valider automatiquement les données => permet de définir les modèles de données (ex: les schémas...)


app = FastAPI() # Création de l'instance de mon appli FastAPI qui va me permettre de définir les routes (ici @app.post)

class Document(BaseModel): # Déclareration de ma classe 'Document' qui va hériter de BaseModel (automatiquement validée et convertie par FastAPI/Pydantic)
    # Structure atttendue quand on reçoit un document via une requête
    id:int  
    title:str
    content:str

fake_db = [] # Fausse base de donnée d'une liste vide pour stocker les documents reçus (on utilisera une vraie base de donnée plus tard)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur ton API FastAPI 👋"}
 
@app.post("/documents") # Déclare un endpoint POST à l'URL /document    POST http://localhost:8000/documents (un fichier json sera attendu)
def create_document(doc: Document): # FastAPI attend un json, le converti en un objet Document, valide les types et le passe dans doc
    fake_db.append(doc) # Ajout de l'objet recu à la liste fake_db
    return {"message": "document created", "doc": doc} # Renvoie une réponse JSON au client avec un message et le document reçu 