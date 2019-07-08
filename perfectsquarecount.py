import math
l,r = map(int,input().split())
count = 0
for i in range(l,r+1):
  sq = math.sqrt(i)
  if (sq - math.floor(sq))== 0:
    count += 1
print(count)    
  
