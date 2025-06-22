#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def CountPowerSum(X, K, N):
    if X == 0:
        return 1
    if K < 1:
        return 0
    used = CountPowerSum(X-(K**N),K-1,N)
    skipped = CountPowerSum(X,K-1,N)
    return used + skipped

def powerSum(X, N):
    # Write your code here
    nearest = int(X**(1/N))
    ans = 0
    while nearest > 0:
        ans += CountPowerSum(X-(nearest**N),nearest-1,N)
        nearest -= 1
    return ans
    

if __name__ == '__main__':
    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    print(result)
