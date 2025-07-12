# class TreeNode:
#   def __init__(self, data):
#     self.data = data
#     self.children = []
#     self.parent = None
  
#   def add_child(self, child):
#     child.parent = self
#     self.children.append(child)
  
#   def get_level(self):
#     level = 0
#     p = self.parent
#     while p:
#       level += 1
#       p = p.parent
#     return level
  
#   def print_tree(self):
#     spaces = ' ' * self.get_level() * 3
#     prefix = spaces + '|__' if self.get_level() else ""
#     print(prefix + self.data)
#     for child in self.children:
#       child.print_tree()
  
# def build_tree():
#   root = TreeNode('Electronics')

#   laptop = TreeNode('Laptop')
#   laptop.add_child(TreeNode('MacBook'))
#   laptop.add_child(TreeNode('ThinkPad'))
#   laptop.add_child(TreeNode('Dell'))

#   cellphone = TreeNode('Cell Phone')
#   cellphone.add_child(TreeNode('iPhone'))
#   cellphone.add_child(TreeNode('Samsung'))
#   cellphone.add_child(TreeNode('Infinix'))

#   tv = TreeNode('TV')
#   tv.add_child(TreeNode('Sony'))
#   tv.add_child(TreeNode('LG'))
#   tv.add_child(TreeNode('TCL'))

#   root.add_child(laptop)
#   root.add_child(cellphone)
#   root.add_child(tv)

#   return root

# if __name__ == '__main__':
#   root = build_tree()
#   root.print_tree()


# Tree Exercises starts from here...
# Exercise 1
# class TreeNode:
#   def __init__(self, name, designation):
#     self.name = name
#     self.designation = designation
#     self.children = []
#     self.parent = None
  
#   def add_child(self, child):
#     child.parent = self
#     self.children.append(child)
  
#   def get_level(self):
#     level = 0
#     p = self.parent
#     while p:
#       level += 1
#       p = p.parent
#     return level
  
#   def print_tree(self, to_print):
#     if to_print == 'name':
#       value = self.name
#     elif to_print == 'designation':
#       value = self.designation
#     elif to_print == 'both':
#       value = self.name + ' (' + self.designation + ')'
#     else:
#       return
    
#     spaces = ' ' * self.get_level() * 3
#     prefix = spaces + '|__' if self.get_level() else ""
#     print(prefix + value)

#     for child in self.children:
#       child.print_tree(to_print)

# def build_management_tree():

#   infra_head = TreeNode('Vishwa', 'Infrastructure Head')
#   infra_head.add_child(TreeNode('Dhaval', 'Cloud Manager'))
#   infra_head.add_child(TreeNode('Abhijit', 'App Manager'))

#   app_head = TreeNode('Aamir', 'Application Head')

#   CTO Heirarchy
#   cto = TreeNode('Chinmay', 'CTO')
#   cto.add_child(infra_head) 
#   cto.add_child(app_head) 

#   HR Heirarchy
#   hr = TreeNode('Gels', 'HR Head')
#   hr.add_child(TreeNode('Peter', 'Recruitment Manager'))
#   hr.add_child(TreeNode('Waqas', 'Policy Manager'))

#   CEO Heirarchy
#   ceo = TreeNode('Nilupul', 'CEO')
#   ceo.add_child(cto)
#   ceo.add_child(hr)

#   return ceo


# Exercise 2
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.children = []
    self.parent = None
  
  def add_child(self, child):
    child.parent = self
    self.children.append(child)
  
  def get_level(self):
    level = 0
    p = self.parent
    while p:
      level += 1
      p = p.parent
    return level
  
  def print_tree(self, level):
    if self.get_level() > level:
      return
    spaces = ' ' * self.get_level() * 3
    prefix = spaces + '|__' if self.get_level() else ""
    print(prefix + self.data)
    for child in self.children:
      child.print_tree(level)

def build_location_tree():
  punjab = TreeNode('Punjab')
  punjab.add_child(TreeNode('Lahore'))
  punjab.add_child(TreeNode('Gujranwala'))

  sindh = TreeNode('Sindh')
  sindh.add_child(TreeNode('Karachi'))
  sindh.add_child(TreeNode('Hyderabad'))

  pakistan = TreeNode('Pakistan')
  pakistan.add_child(punjab)
  pakistan.add_child(sindh)

  new_jersey = TreeNode('New Jersey')
  new_jersey.add_child(TreeNode('Princeton'))
  new_jersey.add_child(TreeNode('Trenton'))

  california = TreeNode('California')
  california.add_child(TreeNode('San Francisco'))
  california.add_child(TreeNode('Mountain View'))
  california.add_child(TreeNode('Palo Alto'))

  usa = TreeNode('USA')
  usa.add_child(new_jersey)
  usa.add_child(california)

  gujarat = TreeNode('Gujarat')
  gujarat.add_child(TreeNode('Ahmedabad'))
  gujarat.add_child(TreeNode('Baroda'))

  karnatka = TreeNode('Karnatka')
  karnatka.add_child(TreeNode('Bangaluru'))
  karnatka.add_child(TreeNode('Mysore'))

  india = TreeNode('India')
  india.add_child(gujarat)
  india.add_child(karnatka)


  globe = TreeNode('Global')
  globe.add_child(pakistan)
  globe.add_child(usa)
  globe.add_child(india)

  return globe

if __name__ == "__main__":
  root = build_location_tree()
  root.print_tree(4)
