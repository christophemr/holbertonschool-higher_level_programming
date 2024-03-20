#!/usr/bin/python3
"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sys import argv

# Create a Base instance
Base = declarative_base()

# Define the State class


class State(Base):
    """State class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


# Create connection string using command-line arguments
connect_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
    argv[1], argv[2], argv[3])

# Create engine
engine = create_engine(connect_url)

# Import all classes inheriting from Base before
# calling Base.metadata.create_all(engine)
Base.metadata.create_all(engine)
