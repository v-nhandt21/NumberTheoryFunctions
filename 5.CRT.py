def inv(a, m) :
     m0 = m
     x0 = 0
     x1 = 1
     
     if (m == 1) :
          return 0
     
     # Apply extended Euclid Algorithm
     while (a > 1) :
          q = a // m
          t = m
          m = a % m
          a = t
          t = x0
          x0 = x1 - q * x0
          x1 = t
     if (x1 < 0) :
          x1 = x1 + m0
     return x1
     
# k is size of num[] and rem[].
# Returns the smallest
# number x such that:
# x % num[0] = rem[0],
# x % num[1] = rem[1],
# ..................
# x % num[k-2] = rem[k-1]
# Assumption: Numbers in num[]
# are pairwise coprime
# (gcd for every pair is 1)

def findMinX(num, rem) :
     k=len(num)
     prod = 1
     for i in range(0, k) :
          prod = prod * num[i]
     result = 0
     for i in range(0,k):
          pp = prod // num[i]
          result = result + rem[i] * inv(pp, num[i]) * pp
     return result % prod
     
# Driver method
A = [3, 4, 5]
M = [2, 3, 1]
print( "x is " , findMinX(A, M))