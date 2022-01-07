# Input: a,n
# Output: b such that a*b mod n =1 

# def modInverse2(a, m):
#      for x in range(1, m):
#           if (((a%m) * (x%m)) % m == 1):
#                return x
#      return None

def modInverse(n, a):

     RList = []
     r0 = n
     r1 = a
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

     if RList[-2][0] == 1:
          return RList[-2][3]
     else:
          return None

# b = a^-1 (mod n)
# a much < n
a = 61
n = 25609494822912685
print(modInverse(n, a))


# print(modInverse(n, a)*a % n)
# print(modInverse(pow(1979,3),pow(37,3)))