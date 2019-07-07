n,k = map(int,input().split())
a = map(int,input().split())
b = map(int,input().split())
com = []
for x in a:
  if x in b:
    com.append(x)
for p in com:
  print(p,end=' ')
