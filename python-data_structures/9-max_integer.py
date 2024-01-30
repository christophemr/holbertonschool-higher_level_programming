#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return (None)
    else:
        int_max = my_list[0]
        for i in range(len(my_list)):
            if (my_list[i] > int_max):
                int_max = my_list[i]
        return (int_max)
