class Node:
  def __init__(self, value) -> None:
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self) -> None:
    self.head = None


  def insert_at_beginning(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
      return
    last = self.head
    while last.next:
      last = last.next
    last.next = new_node

  def search(self, value):
    current = self.head
    while current:
      if current.value == value:
        return True
      current = current.next
    return False
  
  def delete(self,value):
    temp = self.head
    if temp and temp.value == value:
      self.head = temp.next
      return
    
    prev = None
    while temp and temp.value != value:
      prev = temp
      temp = temp.next

    if not temp:
      return

    prev.next = temp.next
  
  def display(self):
    current = self.head
    ll = []
    while current:
      ll.append(current.value)
      current = current.next
    return ll
    
  def insert_at_position(self, position, value):
    new_node = Node(value)
    if position == 1:
      new_node.next = self.head
      self.head = new_node
      return

    count = 1
    current = self.head
    while current and count < position - 1:
      current = current.next
      count += 1
    
    if not current:
      print("Position  out of bounds")
      return
    
    new_node.next = current.next
    current.next = new_node

  def reverse(self):
    prev = None
    cur = self.head
    while cur:
      new = cur.next
      cur.next = prev
      prev = cur
      cur = new
    self.head = prev
    
ll = LinkedList()
ll.insert_at_beginning(1)
ll.insert_at_beginning(2)
ll.insert_at_beginning(3)
ll.insert_at_beginning(4)
print("No of ele in ll:: ", ll.display())
ll.reverse()
# ll.insert_at_position(3, 10)
print("No of ele in ll:: ", ll.display())
# print(ll.search(10))