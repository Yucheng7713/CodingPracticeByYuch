#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    numOfBribe = 0
    # Data preprocessing
    q = [n - 1 for n in q]

    for i in range(len(q)):
        if q[i] > i:
            diff = q[i] - i
            if diff > 2:
                print("Too chaotic")
                return
            else:
                numOfBribe += diff
        elif q[i] < i:
            diff = len([n for n in q[:i] if n > q[i]]) - (i - q[i])
            if diff > 2:
                print("Too chaotic")
                return
            else:
                numOfBribe += diff
    print(numOfBribe)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)


