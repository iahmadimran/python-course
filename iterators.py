class RemoteControl:
  def __init__(self):
    self.channels = ['HBO', "Al-Jazeera", 'CNN', 'BBC']
    self.index = -1

  def __iter__(self):
    return self
  
  def __next__(self):
    self.index += 1
    if self.index == len(self.channels):
      raise StopIteration
    
    return self.channels[self.index]

r = RemoteControl()
iterator = iter(r)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))