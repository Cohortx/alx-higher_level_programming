#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return success
    except (ValueError, TypeError):
        return fail
