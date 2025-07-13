class BinarySearchTreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def add_child(self, data):
    if data == self.data:
      return
    
    if data < self.data:
      if self.left:
        self.left.add_child(data)
      else:
        self.left = BinarySearchTreeNode(data)
    else:
      if self.right:
        self.right.add_child(data)
      else:
        self.right = BinarySearchTreeNode(data)

  def search(self, val):
    if val == self.data:
      return True

    if val < self.data:
      if self.left:
        return self.left.search(val)
      else:
        return False
    else:
      if self.right:
        return self.right.search(val)
      else:
        return False
      
  def find_min(self):
    while self.left is not None:
      self = self.left
    
    return self.data
  
  def find_max(self):
    while self.right is not None:
      self = self.right
    
    return self.data
  
  def calculate_sum(self):
    if self.left:
      left_sum = self.left.calculate_sum()
    else:
      left_sum = 0

    if self.right:
      right_sum = self.right.calculate_sum()
    else:
      right_sum = 0

    return self.data + left_sum + right_sum
  
  def in_order_traversal(self):
    elements = []

    if self.left:
      elements += self.left.in_order_traversal()
    
    elements.append(self.data)

    if self.right:
      elements += self.right.in_order_traversal()
    
    return elements
  
  def pre_order_traversal(self):
    elements = [self.data]

    if self.left:
      elements += self.left.pre_order_traversal()

    if self.right:
      elements += self.right.pre_order_traversal()
    
    return elements
  
  def post_order_traversal(self):
    elements = []

    if self.left:
      elements += self.left.post_order_traversal()
    
    if self.right:
      elements += self.right.post_order_traversal()
    
    elements.append(self.data)

    return elements
  
  
def build_tree(elements):
  root = BinarySearchTreeNode(elements[0])

  for i in range(1, len(elements)):
    root.add_child(elements[i])
  
  return root

if __name__ == "__main__":
  numbers = [23, 35, 7, 12, 16, 43, 67]
  numbers_tree = build_tree(numbers)

  print(numbers_tree.calculate_sum())

  # print(numbers_tree.search(655))
  # print(numbers_tree.in_order_traversal())
  # print(numbers_tree.pre_order_traversal())
  # print(numbers_tree.post_order_traversal())
  