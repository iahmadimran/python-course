class BinarySearchTreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def add_child(self, data):
    if self.data == data:
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
    if self.data == val:
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
  
  def find_min(self):
    while self.left is not None:
      self = self.left
    return self.data
  
  def find_max(self):
    while self.right is not None:
      self = self.right
    return self.data
  
  def calculate_sum(self):
    left_sum = self.left.calculate_sum() if self.left else 0
    right_sum = self.right.calculate_sum() if self.right else 0
    return (self.data + left_sum + right_sum)
  
def build_tree(elements):
  root = BinarySearchTreeNode(elements[0])

  for i in range(1, len(elements)):
    root.add_child(elements[i])
  
  return root

if __name__ == '__main__':
  countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
  countries_tree = build_tree(countries)

  # print(countries_tree.in_order_traversal())
  # print(countries_tree.search('Nigeria'))

  numbers = [23, 43, 65, 12, 3, 87, 15, 6, 43]
  numbers_tree = build_tree(numbers)

  # print(numbers_tree.find_min())
  # print(numbers_tree.find_max())

  # print(numbers_tree.in_order_traversal())
  # print(numbers_tree.pre_order_traversal())
  print(numbers_tree.post_order_traversal())

  print(numbers_tree.calculate_sum())
  # print(numbers_tree.search(34))
