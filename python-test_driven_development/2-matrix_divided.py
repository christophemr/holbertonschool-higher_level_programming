#!/usr/bin/python3
"""this module defines a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): Number used for division.

    Raises:
        TypeError: If the matrix contains non-numbers or
        rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.

    Returns:
        list: A new matrix representing the result of the divisions.
    """
    # Check if matrix is a valid list of lists with numbers
    if (
        not all(isinstance(row, list) and
                all(isinstance(ele, (int, float))
                for ele in row) for row in matrix)):
        raise TypeError("matrix must be a list of lists of integers/floats")

    # Check if all rows have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform matrix division and round the result to 2 decimal places
    return [[round(ele / div, 2) for ele in row] for row in matrix]
