# a < b < M
# 7 digit of a/b
# => find a, b

# cal EEA( 10^7, 7digits)
# Find r < Threshold M => s, t = a,b 

def RR(f, threshold):

     RList = []
     r0 = pow(10,len(str(f)))
     r1 = f
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

     for r in RList:
          print(r)
     print("===================")

     for r in RList:
          if r[0] < threshold:
               return r[2], r[3]
     return None

##############

# Example
# A = 511
# B = 710
# A/B = 0.7197183098591549...

# Input: 7197183
# Output: 511, 710

# threshold is A*10
print(RR(7197183 , threshold=1000))