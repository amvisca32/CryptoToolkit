# Adrianna Visca
# Square and Multiply Program
# CSCI 462-04

import sys

def squareAndMultiply(base,exponent,modulus):
    exp = bin(exponent)
    print ("Binary: " + exp)
    tempBase = base
    print ("Bit\tResult")
    print ("1:\t1 (S)")
    print ("1:\t" + str(tempBase) + " (M)")
    for i in range(4, len(exp)+1):
        tempBase = (tempBase * tempBase)
        tempBase = (tempBase%modulus)
        print (str(i-2) + ":\t" + str(tempBase) + " (S)")
        if exp[i-1]=='1':
            tempBase = (tempBase * base)
            tempBase = (tempBase%modulus)
            print (str(i-2) + ":\t" + str(tempBase) + " (M)")
    return tempBase

def main():
    base = int(sys.argv[1])
    exp = int(sys.argv[2])
    mod = int(sys.argv[3])
    print ("We will calculate base^exp mod m")
    print ("base = ", base)
    print ("exp = ", exp)
    print ("m = ", mod)
    print ("==== Calculation ====")
    ans = squareAndMultiply(base, exp, mod)
    print("Square and Multiply Function returned: "+ str(ans))

if __name__ == '__main__':
    main()