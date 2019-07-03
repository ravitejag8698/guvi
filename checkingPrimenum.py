#to check whether a num is prime or not
from math import *
n = int(input())
if n>1:
  for i in range(2,ceil(sqrt(n))+1):
    if n%i == 0:
      print('no')
  else:
    print('yes')
  
