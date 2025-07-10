class HashTable:
  def __init__(self):
    self.MAX = 100
    self.arr = [None for i in range(self.MAX)]
  
  def get_hash(self, key):
    h = 0
    for char in key:
      h += ord(char)
    
    return h % self.MAX
  
  def __setitem__(self, key, value):
    h = self.get_hash(key)
    self.arr[h] = value
  
  def __getitem__(self, key):
    h = self.get_hash(key)
    return self.arr[h]
  
  def __delitem__(self, key):
    h = self.get_hash(key)
    self.arr[h] = None

 
t = HashTable()
t['march 6'] = 'ahmad'
t['march 9'] = 'shoaib'
del t['march 6']
print(t.arr)
