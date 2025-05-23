from fastapi import FastAPI

from app import models
from app.database import engine
from app.routes import note_routes, user_routes
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")




models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(user_routes.router)

app.include_router(note_routes.router)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Notes API!"}


@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"token": token}


