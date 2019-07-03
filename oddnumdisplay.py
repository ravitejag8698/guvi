s,e = map(int,input().split())
for i in range(s,e):
  if (i%2 != 0) and (i > 2):
    print(i,end=' ')
