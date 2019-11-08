# Python program to demonstrate working of extended 
# Euclidean Algorithm 

# function for extended Euclidean Algorithm 
def gcdExtended(a, b, x, y): 
    # Base Case 
    if a == 0 : 
        x = 0
        y = 1
        return b 
    x1 = 1
    y1 = 1 # To store results of recursive call 
    gcd = gcdExtended(b%a, a, x1, y1) 
    # Update x and y using results of recursive 
    # call 
    x = y1 - (b/a) * x1 
    y = x1 
    return gcd 

def modInverse(a, m) : 
    m0 = m
    y = 0
    x = 1
    if (m == 1) : 
        return 0
    while (a > 1) : 
        # q is quotient 
        q = a // m 
        t = m 
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
        # Update x and y 
        y = x - q * y 
        x = t 
    
    # Make x positive 
    if (x < 0) :
        x = x + m0 
            
    return x 

def main():
    x = 1
    y = 1
    a = 29
    b = 17
    g = gcdExtended(a, b, x, y)
    print("gcd(", a , "," , b, ") = ",g)
    a = 3
    m = 11
    print("Modular multiplicative inverse is", modInverse(a, m))

if __name__ == '__main__':
    main()
