def fibonacci():
  a, b = 0, 1
  while a < 100:
    yield a
    a, b = b, a + b

for f in fibonacci():
  print(f)