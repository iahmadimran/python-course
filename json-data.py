import json
import os

book = {
  "ahmad": {
    "name": 'ahmad',
    'address': 'wapda town',
    'phone': 387384738
  },

  "shoaib": {
    "name": 'shoaib',
    'address': 'citi housing',
    'phone': 373478989
  }
}


print(os.getcwd())

str = json.dumps(book)
# print(str)

# arr = os.listdir()
# # print(arr)

with open('book.txt', 'r') as f:
  s = f.read()
  print(s)