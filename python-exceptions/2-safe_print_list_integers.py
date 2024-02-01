#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end='')
            nb_print += 1
        except (ValueError, TypeError):
            pass
    print()
    return (nb_print)
