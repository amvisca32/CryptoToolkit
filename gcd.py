# GCD 

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def main():
    x = int(input())
    y = int(input())
    g = gcd(x, y)
    print ("GCD is: " + str(g))

if __name__ == '__main__':
    main()
