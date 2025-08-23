import time
import threading

def calculate_square(numbers):
  print('Calculating square of numbers')
  for number in numbers:
    time.sleep(0.1)
    print(f'square:', number * number)

def calculate_cube(numbers):
  print('Calculating cube of numbers')
  for number in numbers:
    time.sleep(0.1)
    print(f'cube:', number * number * number)

arr = [4, 5, 6, 7]
t = time.time()

t1 = threading.Thread(target=calculate_square, args=(arr,))
t2 = threading.Thread(target=calculate_cube, args=(arr,))

t1.start()
t2.start()

t2.join()
t1.join()

print("Done in ", time.time() - t)