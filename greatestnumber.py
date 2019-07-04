n = int(input())
l = map(int,input().split())
ls = list(l)
ls.sort()
rev = ls[::-1]
s = ''.join(ls)
print(int(s))
