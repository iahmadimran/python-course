from collections import deque

class Stack:
  def __init__(self):
    self.container = deque()

  def push(self, value):
    self.container.append(value)
  
  def pop(self):
    return self.container.pop()

  def peek(self):
    return self.container[-1]
  
  def is_empty(self):
    return len(self.container) == 0
  
  def size(self):
    return len(self.container)

def reverse_string(s):
  stack = Stack()

  for char in s:
    stack.push(char)
  
  rstr = ''
  while stack.size() != 0:
    rstr += stack.pop()
  
  return rstr

def is_balanced(expression):
  stack = Stack()
  opening = {'(': ')', '{': '}', '[': ']'}
  closing = {')', '}', ']'}

  for char in expression:
    if char in opening:
      stack.push(char)
    elif char in closing:
      if not stack:
        return False
      last_open = stack.pop()
      if opening[last_open] != char:
        return False 
  
  return stack.size() == 0

print(is_balanced('(x+y)+{x+35}*[jdksjdf]'))


stack = Stack()
stack.push(65)
stack.push(53)
stack.push(90)
stack.push(87)

# print(stack.peek())
# print(stack.size())
# print(stack.is_empty())
# print(stack.container)
# print(reverse_string('We will conquere COVID-19'))
