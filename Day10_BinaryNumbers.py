#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    def decimalToBinary(n):  
        return bin(n).replace("0b", "") 

    binary = decimalToBinary(n)
      
    max_len = 0
    i = 0
    while(i<len(binary)-1):
        if binary[i] == '1':
            _len = 1
            i = i + 1
            while(i < len(binary) and binary[i] == '1'):
                _len = _len + 1
                i = i + 1
            max_len = max(_len,max_len)
            
        else:
            i = i + 1

    print(max_len)
        