from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String,ForeignKey
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String,unique=True,index=True)
    hashed_password = Column(String)

    notes = relationship("Note", back_populates="owner")



class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="notes")

