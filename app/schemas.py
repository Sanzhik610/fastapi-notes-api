from pydantic import BaseModel,EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str
class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str= "bearer"
class NoteBase(BaseModel):
    title: str
    content: Optional[str]=None
class NoteCreate(NoteBase):
    pass
class NoteOut(NoteBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True
