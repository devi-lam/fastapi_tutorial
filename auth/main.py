from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from auth import models, schemas, utils
from auth_database import get_db
from jose import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm


# Helper function that takes user data
def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow(), timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

app = FastAPI()

@app.post("/signup")
def register_user(user: schemas.UserCreate, db:Session = Depends(get_db)):
    # check the user exit or not
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail = "Username already exist")
    
    # Hash the password
    hashed_pass = utils.hash_password(user.password)

    # Create ew user instance
    new_user = model_User(
        username = user.username,
        email = user.email,
        hashed_password = hashed_pass,
        role=user.role

    )

# Save user to db
db.add(new_user)
db.commit()
db.refresh(new_user)

# Return the value (excluding password)
return {'id': new_user.id, "username":new_user.username, "email":new_user.email, "role": new_user.role}


@app.post("/login")