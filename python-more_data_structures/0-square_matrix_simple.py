#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # empty matrix
    new_matrix = []
    for row in matrix:
        # use map to apply (x ** 2) to each elements in the row
        new_row = list(map(lambda x: x ** 2, row))
        # append new_row to the result matrix
        new_matrix.append(new_row)
    return (new_matrix)
