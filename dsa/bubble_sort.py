from util import time_it

@time_it
def bubble_sort(elements, key):
  size = len(elements)

  for i in range(size - 1):
    swapped = False
    for j in range(size - 1 - i):
      a = elements[j][key]
      b = elements[j + 1][key]
      if a > b:
        tmp = elements[j]
        elements[j] = elements[j + 1]
        elements[j + 1] = tmp
        swapped = True
    if not swapped:
      break


if __name__ == "__main__":
  numbers = [24, 65, 6, 9, 7, 17, 22, 34]
  print(numbers)

  
  elements = [
    { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
    { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
    { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
  ]

  bubble_sort(elements, key='name')
  print(elements)