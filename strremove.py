n = int(input())
s = input()
s = list(s)
v = ['a','e','i','o','u']
for i in s:
  if i in v:
    s.remove(i)
s = s[::-1]
f = ''.join(s)
print(f)
