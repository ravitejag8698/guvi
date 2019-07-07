from math import *
n1 = map(int,input().split())
n2 = map(int,input().split())
n1 = list(n1)
n2 = list(n2)
d = []
for i in range(len(n1)):
  d.append(abs(n1[i]-n2[i]))
for x in d:
  print(x,end = ' ')
  
