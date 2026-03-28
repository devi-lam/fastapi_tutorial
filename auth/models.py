from sqlalchemy import Column, Integer, String
from auth_database import Base

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, Index = True)
    username = Column(String(255), unique=255, index=True)
    hashed_password = Column(String(255))
    role = Column(String(50), default="user")
    

