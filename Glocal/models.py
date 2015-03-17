from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

<<<<<<< HEAD
class User(db.Model):
    id = db.Column(db.Integer, autoincrement=1, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password, first_name, last_name):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return 'id {}<username {}, password {}, firstname {}, lastname{}'.\
            format(self.id, self.username, self.password, self.first_name,
                   self.last_name)
=======
class User(Base):
    """Set up the User table"""
    __tablename__ = 'user'
    username = Column(String(250), primary_key=True)
    password = Column(String(250), nullable=False)

# Creates an enginer that stores data in the local directory
engine = create_engine('sqlite:///sqlalchemy_user.db')

# Create all tables in the engine
Base.metadata.create_all(engine)
>>>>>>> master
