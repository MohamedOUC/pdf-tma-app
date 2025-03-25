from pydantic import BaseModel

class DocumentBase(BaseModel):
    title: str
    content: str
    
class DocumentCreate(BaseModel):
    pass

class Document(BaseModel):
    id: int
    
    class Config:
        orm_mode = True