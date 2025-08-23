import time
import multiprocessing

def calculate_square(numbers):
  print('Calculating square of numbers')
  for number in numbers:
    time.sleep(8)
    print('square: ' + str(number * number))


if __name__ == "__main__":
  arr = [4, 5, 6, 7]
  p1 = multiprocessing.Process(target=calculate_square, args=(arr,))
  p1.start()
  p1.join()

  print("Done")