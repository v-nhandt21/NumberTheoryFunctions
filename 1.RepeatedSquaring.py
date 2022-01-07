# Function code 

# Input: a,e,n
# Output: a^e mod n
# repeatedSquaring(a, e, n)

def repeatedSquaring1(bas, exp, modulo):

     if (exp == 0):
          return 1
     if (exp == 1):
          return bas % modulo
     t = repeatedSquaring1(bas, int(exp / 2), modulo)
     t = (t * t) % modulo

     if (exp % 2 == 0):
          return t
     else:
          return ((bas % modulo) * t) % modulo

def repeatedSquaring2(bas, exp, modulo):
     return pow(bas, exp, modulo)

M = repeatedSquaring1(134000000000, 1000000000000, 1000000000400)
print(M)
M = repeatedSquaring2(134000000000, 1000000000000, 1000000000400)
print(M)