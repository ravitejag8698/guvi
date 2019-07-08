n,m = map(int,input().split())
min = min(n,m)
for i in range(1,min+1):
  great = 1
  if (n%i == 0) and (m%i == 0):
    great = i
print(great)    
