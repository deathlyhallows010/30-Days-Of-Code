#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    A = []

    for _ in range(6):
        A.append(list(map(int, input().rstrip().split())))
        
    max_sum = -1*math.inf
    
    for i in range(4):
        for j in range(4):
            max_sum = max(max_sum,(A[i][j] + A[i][j+1] + A[i][j+2] + A[i+1][j+1] + A[i+2][j] + A[i+2][j+1] + A[i+2][j+2]))
    
    print(max_sum)
