from sqlalchemy.orm import Session
from app import models, schemas
from app.auth import hash_password

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_pw, )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user