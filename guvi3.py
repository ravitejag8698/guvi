vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']
char = input('')
if char in vowels:
  print('Vowel')
elif char in consonants:
  print('Consonant')
else:
  print('invalid')
  
