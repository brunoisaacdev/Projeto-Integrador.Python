from sqlalchemy import Column, ForeignKey, Integer, String, Text

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    numero = Column(String, unique=True, nullable=False)