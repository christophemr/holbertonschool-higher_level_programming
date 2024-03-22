#!/usr/bin/python3
"""
script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
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
    # Query the database for State objects containing
    # the letter 'a' in their name
    states = session.query(State).filter(State.name.contains('a'))
    # Check if any State objects were retrieved
    if states is not None:
        # Loop through each retrieved State object
        for state in states:
            # Loop through each retrieved ('a) State object
            # and delete it
            session.delete(state)
    # Commit the changes to the database
    session.commit()
    # Close the session
    session.close()
