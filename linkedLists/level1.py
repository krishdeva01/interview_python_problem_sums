class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def display(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next

  
  def insert_at_end(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      return
    last = self.head
    while last.next:
      last = last.next
    last.next = new_node

  
  def search(self,key):
    current = self.head
    while current:
      if current.data == key:
        return True
      current = current.next
    return False
  
  def delete(self, key):
    # Initialize head
    temp = self.head

    # if value is in the head node, move the second node to the next node to delete the first node
    if temp and  temp.data == key:
      self.head = temp.next
      return
    # Iterate through the list
    prev = None
    while temp and  temp.data != key:
      prev = temp
      temp = temp.next

    # return none if there is no key found
    if not temp:
      return
    # join the prev node to the next node to ignore the current node which needs to be deleted
    prev.next = temp.next

ll = LinkedList()
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.delete(20)
ll.display()
print(ll.search(1))
print(ll.search(10))