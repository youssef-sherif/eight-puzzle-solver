class QueueNode(object):
  def __init__(self, item = None):
    self.item = item
    self.next = None
    self.previous = None


class Queue(object):
  def __init__(self):
    self.length = 0
    self.head = None
    self.tail = None

  def enqueue(self, x):
    newNode = QueueNode(x)
    if self.head == None:
      self.head = self.tail = newNode
    else:
      self.tail.next = newNode
      newNode.previous = self.tail
      self.tail = newNode
    self.length += 1


  def dequeue (self):
    item = self.head.item
    self.head = self.head.next 
    self.length -= 1
    if self.length == 0:
      self.last = None
    return item