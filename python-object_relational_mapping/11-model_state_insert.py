#!/usr/bin/python3
"""
script that prints that adds the State object
Louisiana to the database `hbtn_0e_6_usa`.
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
    # Create a new State object for Louisiana
    new_state = State(name="Louisiana")
    # Add the new state object to the session
    session.add(new_state)
    # Commit the changes to the database
    session.commit()
    # Print the ID of the newly added state
    print('{0}'.format(new_state.id))
    # Close the session
    session.close()
