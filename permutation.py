from itertools import permutations
n = input()
per = []
permlist = permutations(n)
for perm in list(permlist):
  
  f = ''.join(perm)
  per.append(f)
per = set(per)
per = list(per)
per.sort()
for z in per:
  print(z)
