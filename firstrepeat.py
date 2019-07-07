n = int(input())
f = map(int,input().split())
d = list(f)
k = []
for i in range(n):
  for j in range(i+1,n):
    if d[i] == d[j]:
      k.append(d[i])
      break
  
  
if(len(k) == 0):
  print('unique')
else:
  print(k[0])
