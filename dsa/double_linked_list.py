class Node:
  def __init__(self, data=None, next=None, prev=None):
      self.data = data
      self.next = next
      self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count
    
    def insert_at_the_beginning(self, data):
      node = Node(data, self.head, None)
      self.head = node

    def insert_at_end(self, data):
        if self.head is None:
          self.head = Node(data, None, None)
          return

        itr = self.head
        while itr.next:
          itr = itr.next

        itr.next = Node(data, None, self.head)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr.prev)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
          return
        
        if self.head.data == data_after:
          self.head.next = Node(data_to_insert, self.head.next, self.head.prev)
          return
      

        itr = self.head
        while itr:
          if itr.data == data_after:
            node = Node(data_to_insert, itr.next, itr.prev)
            itr.next = node
            break 

          itr = itr.next
    
    def remove_by_value(self, data):
      if self.head is None:
        return
      
      if self.head.data == data:
        self.head = self.head.next
        return
      
      itr = self.head
      while itr.next:
        if itr.next.data == data:
          itr.next = itr.next.next
          break
        
        itr = itr.next
    
    def print_forward(self):
        itr = self.head
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+ ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
    
    def print_backword(self):
        if self.head is None:
            return 
        
        itr = self.head 
        while itr.next:
           itr = itr.next
        
        dllstr = ''
        while itr:
            dllstr += str(itr.data) + ' --> ' if itr.prev else str(itr.data)
            itr = itr.prev
        
        print(dllstr)



if __name__ == '__main__':
    ll = DoubleLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at_the_beginning('figs')
    ll.print_forward()
    ll.print_backword()
    # ll.print()
    # ll.insert_after_value("grapes","blueberry") # insert apple after mango
    # ll.print()
    # ll.remove_by_value("orange") # remove orange from linked list
    # ll.print()
    # ll.remove_by_value("figs")
    # ll.print()
    # ll.remove_by_value("banana")
    # ll.remove_by_value("mango")
    # ll.remove_by_value("blueberry")
    # ll.remove_by_value("grapes")
    # ll.print()
