# Queue: A queue.
# Your implementation should pass the tests in test_queue.py.
# Grayson Kansala

# Hint: pip3 install llist
from pyllist import sllist

class Queue:
   def __init__(self):
      self.data=sllist()

   def enqueue(self,value):
      return self.data.append(value)

   def dequeue (self):
      return self.data.popleft()

   def is_empty(self):
      if self.data.size>0:
         return False
      else:
         return True