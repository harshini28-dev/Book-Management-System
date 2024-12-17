# models.py

from sqlalchemy import Column, Integer, String
from app.database import Base

# Define the Book model
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)  # Primary key
    title = Column(String(100), nullable=False)        # Book title
    author = Column(String(50), nullable=False)        # Author name
    description = Column(String(255))                 # Optional description
