#!/usr/bin/python3
"""
    script that takes in the name of a state as an argument
    and lists all cities of that state,
    using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Main execution block
    Connects to the database and retrieves the cities
    """
    # Connect to the MySQL database using the provided arguments
    db = MySQLdb.connect(
        host="localhost",  # Hostname of the database server
        user=argv[1],     # Username obtained from command-line argument
        port=3306,        # Port number of the database server
        passwd=argv[2],   # Password obtained from command-line argument
        db=argv[3]
    )       # Database name obtained from command-line argument

    # Use cursor to execute SQL queries
    with db.cursor() as cursor:
        # Execute SQL query to fetch cities of the given state
        cursor.execute("""
                       SELECT cities.id, cities.name
                from cities JOIN states ON cities.state_id = states.id
                WHERE states.name LIKE BINARY %(state_name)s
                ORDER BY cities.id ASC""", {'state_name: argv[4]'})

        # Fetch all rows returned by the query
        rows = cursor.fetchall()
    # Check if any rows were returned
    if rows is not None:
        # Print the names of the cities separated by commas
        print(", ".join([row[1] for row in rows]))
