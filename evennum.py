#displaying even numbers with in an interval
s,e = map(int,input().split())
for i in range(s+1,e):
  if i%2 == 0:
    print(i,end=' ')
