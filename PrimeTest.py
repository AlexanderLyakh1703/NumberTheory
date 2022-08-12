from random import randint, randrange
from math import gcd

def ferma(p,test=10):
    if p == 1:
        return False
    elif p in {2,3,5,7,11}:
        return True
    elif p%10 in {0,2,4,6,8}:
        return False
    elif not((p-1)%6 == 0 or (p+1)%6 == 0):
        return False
    else:
        for _ in range(test):
            a = randint(2,p-1)
            if gcd(a,p) != 1 or pow(a,p-1,p) != 1:
                return False
    return True

def miller_rabin(n,test=10):
    if n == 1:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(test):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

def IsPrime(p):
    if miller_rabin(p) and ferma(p):
        return True
    return False

def main():
    n = int(input())
    print(IsPrime(n))

if __name__ == "__main__":
    main()
