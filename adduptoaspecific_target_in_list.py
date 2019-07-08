n,k = map(int,input().split())
d = map(int,input().split())
d = list(d)
repeat = []
for i in range(n):
  for j in range(i+1,n):
    if d[i] + d[j] == k:
      repeat.append([d[i],d[j]])
if (len(repeat) == 0):
  print('NO')
else:
  print('YES')
      
