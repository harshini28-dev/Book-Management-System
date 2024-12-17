# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL database connection URL
DATABASE_URL = "mysql+pymysql://root:Harshini%405034@localhost:3306/bookdb"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models
Base = declarative_base()


from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:Harshini%405034@localhost:3306/BookDB"
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")
