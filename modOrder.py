# Modular Order Program
# CSCI 462-04

import sys


def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

def mul_order(m)
    for i in range (0, m):
        if gcd(i, m) != 1:
            print("GCD not 1")
        else:
            print("Order " + str(i) + " mod " + str(m) + ": 


def main():
#    a = int(sys.argv[1])
    m = int(sys.argv[1])
    mul_order(m)
