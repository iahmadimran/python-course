# class HashTable:
#   def __init__(self):
#     self.MAX = 10
#     self.arr = [[] for i in range(self.MAX)]
  
#   def get_hash(self, key):
#     h = 0
#     for char in key:
#       h += ord(char)
    
#     return h % self.MAX
  
#   def __setitem__(self, key, value):
#     h = self.get_hash(key)
#     found = False
#     for idx, element in enumerate(self.arr[h]):
#       if len(element) == 2 and element[0] == key:
#         self.arr[h][idx] = (key, value)
#         found = True

#     if not found:
#       self.arr[h].append((key, value))
  
#   def __getitem__(self, key):
#     h = self.get_hash(key)
#     for element in self.arr[h]:
#       if element[0] == key:
#         return element[1]
  
#   def __delitem__(self, key):
#     h = self.get_hash(key)
#     for index, element in enumerate(self.arr[h]):
#       if element[0] == key:
#         del self.arr[h][index]

 
# t = HashTable()
# t['march 6'] = 'ahmad'
# t['march 17'] = 'moeed'
# t['march 9'] = 'sohaib'
# print(t['march 17'])
# print(t.arr)

# HashMap exercises starts from here...
with open('dsa/nyc_weather.csv', 'r') as f:
  next(f)
  temperature = []
  for line in f:
    text = line.split(',')
    temp = int(text[1].replace('\n', ''))
    temperature.append(temp)
    date = text[0]
    # temperature[date] = temp
  
  
avg = float(sum(temperature[0:7]) / len(temperature[0:7]))
average = round(avg, 2)
# print(average)

max_value = max(temperature[0:10])
# print(max_value)
# print(temperature)

with open('dsa/nyc_weather.csv', 'r') as f:
  next(f)
  temperature = {}
  for line in f:
    text = line.split(',')
    temp = int(text[1].replace('\n', ''))
    date = text[0]
    temperature[date] = temp

# print(temperature['Jan 9'])
# print(temperature['Jan 4'])

# The best data structure for this problem is dictionary (internally HashMap)

with open('poem.txt', 'r') as f:
  poem = f.read()

word_stats = {}
words = poem.split(' ')

for word in words:
  if word in word_stats:
    word_stats[word] += 1
  else:
    word_stats[word] = 1

for word, count in word_stats.items():
  # print(f'{word}: {count},')
  pass
# print(word_stats)

# The best data structure I can use here is dictionary (internally hash map) but the time complexity here is O(n) not O(1) because we are iterating through n time in word stats. I used it because we have to store items and values both together.

class HashTable:
  def __init__(self):
    self.MAX = 10
    self.arr = [[] for i in range(self.MAX)]
  
  def get_hash(self, key):
    h = 0
    for char in key:
      h += ord(char)
    
    return h % self.MAX
  
  def __setitem__(self, key, value):
    h = self.get_hash(key)
    start_index = h
    while self.arr[h] is not []:
      h = (h + 1) % self.MAX
      if start_index == h:
        return
      
    self.arr[h] = value

  
  def __getitem__(self, key):
    h = self.get_hash(key)
    start_index = h
    while self.arr[h] is not []:
      if self.arr[h][0] == key:
        return self.arr[h][1]

      h = (h + 1) % self.MAX
      if start_index == h:
        break
        

  
  def __delitem__(self, key):
    h = self.get_hash(key)
    start_index = h
    

 
t = HashTable()
t['march 6'] = 17
t['march 17'] = 28
# del t['march 17']
print(t['march 17'])

print(t.arr)