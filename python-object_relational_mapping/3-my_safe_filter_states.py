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
    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute an SQL query to select rows with names starting with 'N'
    # from the 'states' table and sort by states.id
    cur.execute(
        "SELECT * FROM states WHERE name LIKE \
            BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    # Fetch all rows returned by the query
    rows = cur.fetchall()

    # Iterate through the fetched rows and print each row
    for row in rows:
        print(row)
