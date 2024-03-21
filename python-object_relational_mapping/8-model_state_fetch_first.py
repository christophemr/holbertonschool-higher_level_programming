#!/usr/bin/python3
"""
script that prints the first State objects
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
# Importing the State model and Base
# Importing create_engine to create an engine
from sqlalchemy import create_engine
# Importing sessionmaker to create a session
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Main execution block
    Connects to the database and retrieves the states
    """

    # Construct the database URL using command-line arguments
    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    # Create an engine to connect to the database
    engine = create_engine(database_url)

    # Create a Session class bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()
    # Query the database for the first State object, ordered by ID
    state = session.query(State).order_by(State.id).first()
    # Check if a State object was retrieved
    if state is not None:
        # Print the ID and name of the first State object
        print('{0}: {1}'.format(state.id, state.name))
    else:
        # If no State object was found, print "Nothing"
        print("Nothing")
