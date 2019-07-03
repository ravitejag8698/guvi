vowel = ['a','e','i','o','u']
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']
char = input('')
if char in vowel:
  print('Vowel')
elif char in consonant:
  print('Consonant')
else:
  print('invalid')
  
