# p is 4k+1 prime
# find N such that N^2 = -1 (mod p)

def SquareRoot1(p):
     for N in range(2,p*1000000):
          if (N*N+1) % p == 0 and N!=p:
               return N

# N = SquareRoot1(25609494822912685)
N = SquareRoot1(2094948)
print(N)