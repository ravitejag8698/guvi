n = int(input())
s = map(int,input().split())
li = list(s)
repeat = []
for i in range(n):
  for j in range(i+1,n):
    if li[i] == li[j]:
      k = li[i]
      repeat.append(k)
f = len(repeat)
if(f==0):
  print('unique')
else:
  for z in repeat:
    print(z,end=' ')
      
