import sys
sys.path.append("..")

from random import randint
from ComputationalAlgorithms.fast_sqrt import fast_sqrt
from PrimeTest import IsPrime
from tonelli_shanks import TS

def two_squares(n):

def three_squares(n):
    if n%4 == 0:
        (x,y,z) = three_squares(n//4)
        return (2*x,2*y,2*z)
    elif n%8 == 7:
        print('No represantation!')
    elif n%8 == 3:
        x = randint(1,fast_sqrt(n))
        p = (n-x*x)//2
        while IsPrime(p):
            x = randint(1,fast_sqrt(n))
            p = (n-x*x)//2
        (y,z) = two_squares(p)
