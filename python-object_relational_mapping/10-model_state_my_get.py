#!/usr/bin/python3
"""
script that prints the State objects passes as
argument from the database `hbtn_0e_6_usa`.
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
    # Extract the state name passed as argument
    state_name = argv[4]
    # Query the database to find the state object with the given name
    state = session.query(State).filter(State.name == state_name).first()
    # Check if the state object is found and print its ID
    if state is not None:
        print('{0}'.format(state.id))
    else:
        # Print a message if the state is not found
        print("Not found")
