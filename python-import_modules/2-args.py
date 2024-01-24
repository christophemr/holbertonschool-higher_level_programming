#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) - 1
    if (args < 1):
        print("0 arguments.")
    elif (args == 1):
        print("1: argument:")
    else:
        print("{} argument:".format(args))
    for i in range(args):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
