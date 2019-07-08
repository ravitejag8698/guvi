n = int(input())
sum_n = 0
while n>0:
  r = n%10
  sum_n += r
  n //=10
def rev(sum_n):
  reverse = 0
  while sum_n > 0:
    rem = sum_n%10
    reverse = reverse*10 + rem
    sum_n //= 10
  return reverse
if(sum_n == rev(sum_n)):
  print('YES')
else:
  print('NO')
  
    
  
