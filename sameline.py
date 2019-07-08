x = map(int,input().split())
x = list(x)
y = map(int,input().split())
y = list(y)
z = map(int,input().split())
z = list(z)
if((x[1] == y[1] == z[1]) or (x[0]== y[0] == z[0])):
  print('yes')
else:
  print('no')
