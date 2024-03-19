#!/usr/bin/python3
""" script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument
(safe from MySQL injection)
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Main execution block
    Connects to the database and retrieves the states
    """
    # Connect to the MySQL database using the provided arguments
    db = MySQLdb.connect(
        host="localhost",  # Hostname of the database server
        user=argv[1],     # Username obtained from command-line argument
        port=3306,        # Port number of the database server
        passwd=argv[2],   # Password obtained from command-line argument
        db=argv[3]
    )       # Database name obtained from command-line argument

    with db.cursor() as cursor:
        cursor.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")

        rows = cursor.fetchall()

        if rows is not None:
            for row in rows:
                print(row)
