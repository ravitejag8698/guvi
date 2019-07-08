n,k = map(int,input().split())
d = map(int,input().split())
d = list(d)
d = set(d)
li = list(d)
li.sort(reverse = True)
large = li[k-1]
print(large)
