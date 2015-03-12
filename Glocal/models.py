from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    """Set up the User table"""
    __tablename__ = 'user'
    username = Column(String(250), primary_key=True)
    password = Column(String(250), nullable=False)

# Creates an enginer that stores data in the local directory
engine = create_engine('sqlite:///sqlalchemy_user.db')

# Create all tables in the engine
Base.metadata.create_all(engine)