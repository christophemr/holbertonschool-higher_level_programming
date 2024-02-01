#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # Initialize a variable to count the number of printed elements
    total = 0
    try:
    # Iterate through the list up to the specified index
    for i in range(x):
            # Attempt to print the element at the current index
            print("{}".format(my_list[i]), end='')
            # Increment the total count of printed elements
            total += 1
        except IndexError:
            # Break out of the loop if the index is out of range
            break
    # Print a newline after the loop completes
    print()
    # Return the total count of printed elements
    return (total)
