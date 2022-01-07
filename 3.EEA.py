# Input a, b
# Output: d,x,y that
#     d = (a,b)
#     d = ax+by

def EEA(a, b):

     RList = []
     r0 = a
     r1 = b
     s0=1
     s1 = 0
     t0 = 0
     t1 = 1

     print("r \t q \t s \t t")
     print("==================")
     print( str(r0) +" \t " + "_" +" \t " + str(s0) +" \t " + str(t0))
     print( str(r1) +" \t " + "_" +" \t " + str(s1) +" \t " + str(t1))
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
          print( str(r1) +" \t " + str(q) +" \t " + str(s1) +" \t " + str(t1))
          RList.append((r1,q,s1,t1))
     return RList[-2][0], RList[-2][2], RList[-2][3]


# a should larger than b
a, b = pow(10,7), 7197183
a,b = 1979,240
d, x, y = EEA(a, b)

print("================")
# d = ax + by
print(d)
print(x,y)
