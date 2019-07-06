n = int(input())
su = 0
while n>0:
  rem = n%10
  su += rem ** 2
  n //= 10
print(su)  

  
