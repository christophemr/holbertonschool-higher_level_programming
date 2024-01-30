#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    # sum of corresponding elements of tuple_a and tuple_b
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (new_tuple)
