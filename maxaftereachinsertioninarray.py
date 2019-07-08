n,k = map(int,input().split())
d = map(int,input().split())
d = list(d)
ins = map(int,input().split())
ins = list(ins)
for i in range(k):
  d.append(ins[i])
  print(max(d),end=' ')
  
