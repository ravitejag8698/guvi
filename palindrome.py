n = int(input())
def reverse(n):
  rev = 0
  while(n!=0):   #going through every digit of number
    rem = n%10
    rev = rev*10+rem
    n //= 10
  return rev
if (n == reverse(n)):
  print('yes')
else:
  print('no')
