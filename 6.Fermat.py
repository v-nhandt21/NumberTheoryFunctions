# Given P
# Find A^2 + B^2 = P

# S = squareroot-1( P )
# Call EEA(P,S)
# sqrtP = square_root(P)
# Retrieval A from EEA such that A is largest < sqrtP 

import math 

def SquareRoot1(p):
     for N in range(2,p*1000000):
          if (N*N+1) % p == 0 and N!=p:
               return N

def Fermat(p):
     S = SquareRoot1(p)
     if not S:
          return None

     RList = []
     r0 = p
     r1 = S
     s0=1
     s1 = 0
     t0 = 0
     t1 = 1

     while r1 != 0:
          q= int(r0/r1)

          tm = r1
          r1 = r0%r1
          r0 = tm

          tm = s1
          s1 = s0 - q*s1
          s0 = tm

          tm = t1
          t1 = t0 - q*t1
          t0 = tm
          RList.append((r1,q,s1,t1))
     
     sqrtP = math.sqrt(p) + 1
     for r in RList:
          if r[0] < sqrtP:
               return r[0], r[3]
     return None

# a^2 + b^2 = p
p = 617
a,b = Fermat(p)
print(a,b)