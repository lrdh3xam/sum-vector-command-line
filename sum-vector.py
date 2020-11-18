#!/bin/python3

import os
import sys

def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':

    ar_count = int(input())

    #
    # Add integers to a list stripping EOL chars and split based
    # on spaces.
    #  
    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)
    print(str(result))
