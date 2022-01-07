# https://www.geeksforgeeks.org/find-square-root-under-modulo-p-set-1-when-p-is-in-form-of-4i-3/
# https://gist.github.com/nakov/60d62bdf4067ea72b7832ce9f71ae079
# https://eli.thegreenplace.net/2009/03/07/computing-modular-square-roots-in-python
def squareRoot1(n, p):
     n = n % p
     for x in range (2, p):
          if ((x * x) % p == n) :
               return x
     return None

def power(x, y, p) :
     res = 1 
     x = x % p 
     while (y > 0):
          if (y & 1):
               res = (res * x) % p
          y = y >> 1 
          x = (x * x) % p
     return res

def squareRoot(n, p):
     
     if (p % 4 != 3) :
          print( "Invalid Input" )
          return None
     # Try "+(n^((p + 1)/4))"
     n = n % p
     x = power(n, (p + 1) // 4, p)
     if ((x * x) % p == n):
          return x
     
     # Try "-(n ^ ((p + 1)/4))"
     x = p - x
     if ((x * x) % p == n):
          return x
     return x
     
# Input: a,n
# Output: x that x^2 mod n = a
# Driver Code
p = 7
n = 2
x = squareRoot(n, p)
print(x)