from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from app.models.base_model import Base, BaseModel
import enum
from datetime import datetime

class DocumentType(str, enum.Enum):
    identity_card = "identity_card"
    passport = "passport"
    other = "other"

class Role(Base, BaseModel):
    __tablename__ = "roles"
    name = Column(String(50), unique=True, index=True, nullable=False)
    
    def __repr__(self):
        return f"<Role {self.name}>"

class User(Base, BaseModel):
    __tablename__ = "users"
    
    number_document = Column(String(20), unique=True, index=True, nullable=False)
    specialty = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    phone = Column(String(20), nullable=False)
    full_name = Column(String(100), nullable=False)
    type_document = Column(Enum(DocumentType), nullable=False)
    pass_hash = Column(String(255), nullable=False)
    
    # Relaciones
    bulls = relationship("Bull", back_populates="user")
    opus = relationship("Opus", back_populates="cliente")
    inputs = relationship("Input", back_populates="user")
    
    def __repr__(self):
        return f"<User {self.full_name}>" 