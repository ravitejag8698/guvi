n = int(input())
sums = 0
while n>0:
  rem = n%10
  sums += rem ** 2
  n //= 10
print(sums)  

  
