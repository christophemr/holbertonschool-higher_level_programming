#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Try to format and print the provided value as an integer
        print("{:d}".format(value))
        # If successful, return True to indicate successful printing
        return True
    except (ValueError, TypeError):
       # If an exception (ValueError or TypeError) occurs during formatting or printing,
       # catch the exception and return False to indicate unsuccessful printing
        return False
