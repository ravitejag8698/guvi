n,m = map(int,input().split())
a = map(int,input().split())
b = map(int,input().split())
a = list(a)
b = list(b)
for i in b:
  if i not in a:
    print('NO')
    break
else:
  print('YES')
