from collections import deque
import time
import threading

class Queue:
  def __init__(self):
    self.buffer = deque()
  
  def enqueue(self, value):
    self.buffer.appendleft(value)
  
  def dequeue(self):
    return self.buffer.pop()

  def is_empty(self):
    return len(self.buffer) == 0

  def size(self):
    return len(self.buffer)

queue = Queue()

def place_order(orders):
  for order in orders:
    time.sleep(0.5)
    print('Placing order for', order)
    queue.enqueue(order)
  
def serve_order():
  time.sleep(1)
  while True:
    time.sleep(2)
    order = queue.dequeue()
    print('Now serving order:', order)

if __name__ == '__main__':
  orders = ['pizza','samosa','pasta','biryani','burger']
    
  t1 = threading.Thread(target= place_order, args= (orders,))
  t2 = threading.Thread(target= serve_order)

  t1.start()
  t2.start()





# queue.enqueue('samosa')
# queue.enqueue('pizza')
# queue.enqueue('biryani')
# print(queue.dequeue())
# print(queue.buffer)
