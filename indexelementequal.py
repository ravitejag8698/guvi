n = int(input())
f = map(int,input().split())
d = list(f)
s = []
for i in range(n):
  if (i == d[i]):
    s.append(d[i])

if(len(s) == 0):
  print(-1)
else:
  for z in s:
    print(z,end=' ')
