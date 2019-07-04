n = int(input())
s = map(int,input().split())
li = list(s)
li.sort()
for i in range(len(li)):
  print(li[i],end=' ')
