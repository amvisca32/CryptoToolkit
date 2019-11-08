# EEA solver
# CSCI 462

import sys

def EEA(a, b):
    x0 = 0
    x1 = 1
    y0 = 1
    y1 = 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def mul_inverse(a, m):
    for i in range(0, m):
        if (a*i) % m == 1:
            return i
    return -1

def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    gcd, x0, y0 = EEA(int(a), int(b))
    print(gcd)
    print(x0)
    print(y0)
    if gcd != 1:
        print("Multiplicative modular inverse does not exist.")
    else:
        mod = mul_inverse(a, b)
        if mod == -1:
            print("Multiplicative modular inverse does not exist.")
        else:
            print("Mulitplicative modular inverse " + str(a) + " mod " + str(b) + ": " + str(mod))

if __name__ == '__main__':
    main()
