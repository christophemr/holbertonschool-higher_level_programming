#!/usr/bin/python3
""" script that lists all states
from the database hbtn_0e_0_usa
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

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute an SQL query to select all rows
    # from the 'states' table
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows returned by the query
    rows = cur.fetchall()

    # Iterate through the fetched rows and print each row
    for row in rows:
        print(row)
