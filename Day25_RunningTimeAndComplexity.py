# # Enter your code here. Read input from STDIN. Print output to STDOUT


import math

n = int(input())


def isPrime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


for i in range(n):
    x = int(input())
    if x >= 2 and isPrime(x):
        print("Prime")
    else:
        print("Not prime")