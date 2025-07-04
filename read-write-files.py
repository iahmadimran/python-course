import os

os.chdir('/Users/user/Desktop')
# os.mkdir('/test.txt')

print(os.listdir())

with open('C:/Users/user/Desktop/test.txt', 'r') as f:
  # f.write('hello guys my name is ahmad')
  print(f.read())