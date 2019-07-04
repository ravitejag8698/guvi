n = int(input())
s = map(int,input().split())
li = list(s)
repeat = []
for i in range(n):
  for j in range(i+1,n):
    if li[i] == li[j]:
      repeat.append(li[i])
r = len(repeat)
if(r==0):
  print('unique')
else:
  for x in repeat:
    print(x,end=' ')
      
