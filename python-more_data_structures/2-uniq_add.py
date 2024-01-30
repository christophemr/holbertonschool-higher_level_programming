#!/usr/bin/python3
def uniq_add(my_list=[]):
    number = 0
    # use set to automatically handle uniqueness
    for element in set(my_list):
        # iterate over the unique element and calculate their sum
        number += element
    return (number)
