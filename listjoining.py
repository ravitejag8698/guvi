n = int(input())
d = map(int,input().split())
d = list(d)
d = d[::-1]
s = '->'
f = s.join(d)
print(f)
