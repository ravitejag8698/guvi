n,k = map(int,input().split())
d = map(int,input().split())
li = list(d)
fh = li[:n-k]
sh = li[n-k:]
res = sh+fh
print(res)
