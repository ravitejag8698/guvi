def rom_to_n(s):
  rom = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
  num_val = 0
  for i in range(len(s)):
    if i >0 and rom[s[i]>rom[s[i-1]]:
      num_val += rom[s[i]] - 2*rom[s[i-1]]
    else:
      num_val += rom[s[i]]
  return num_val

s = input()
print(rom_to_n(s)
