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
while c in s:
  p.push(c)
  
reversed = ''
while p.is_empty() is not True:
  reversed = reversed+p.pop()
if s == reversed:
  print('YES')
else:
  print('NO')
  
