n = int(input())
d = map(int,input().split())
d = list(d)
for i in range(n):
  for j in range(i+1,n):
    k = d[i]+d[j]
    if k in d:
      print(d[i],d[j],k,sep=' ',end='\n')
 
