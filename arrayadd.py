n,k = map(int,input().split())
d = map(int,input().split())
li = list(d)
s = 0
for i in range(k):
  s += li[i]
print(s)
