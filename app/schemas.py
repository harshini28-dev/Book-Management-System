from pydantic import BaseModel

# Pydantic schema for creating books
class BookCreate(BaseModel):
    title: str
    author: str
    description: str | None = None

# Pydantic schema for reading books
class BookRead(BookCreate):
    id: int

    # Properly indented Config class
    class Config:
        from_attributes = True  # Updated for Pydantic v2
