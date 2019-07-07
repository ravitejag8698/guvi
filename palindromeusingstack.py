class Stack:
  def __init__(self):
    self.items = []
  def push(self,data):
    self.items.append(data)
  def is_empty(self):
    if len(self.items) == 0:
      return True
  def pop(self):
    return self.items.pop()
    
s = input()
p = Stack()
for c in s:
  p.push(c)
  
reversed = ''
i = 0
while i<len(self.items):
  reversed = reversed+p.pop()
  i+=1
if s == reversed:
  print('YES')
else:
  print('NO')
  
