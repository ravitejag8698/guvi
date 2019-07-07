n = int(input())
l = map(int,input().split())
ls = list(l)
ls.sort(reverse = True)
r = []
for i in ls:
  x = str(i)
  r.append(x)
f = ''.join(r)
f = int(f)
print(f)
  

