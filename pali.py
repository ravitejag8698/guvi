s = input()
s = list(s)
st = ''.join(s)
st = st.strip()
rev = s[::-1]
reversed = ''.join(rev)
reversed = reversed.strip()
if (st==reversed):
  print('YES')
else:
  print('NO')
