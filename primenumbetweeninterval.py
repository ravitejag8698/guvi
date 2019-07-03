#displaying prime numbers between intervals
from math import *
s,e = map(int,input().split())
for n in range(s+1,e):
  for i in range(2,n):
    if n%i == 0:
      break
  else:
    print(n,end=' ')
