n,k = map(int,input().split())
d = map(int,input().split())
li = list(d)
res = li[-k:]+li[:-k]
print(res)
