n,k = map(int,input().split())
c = 0
for p in range(n,k+1):
  if p >1 :
    for j in range(2,p):
      if(p%j == 0):
        break
    else:
      c += 1
print(c) 
   
  
