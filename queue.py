# Queue: A queue.
# Your implementation should pass the tests in test_queue.py.
# Grayson Kansala

# Hint: pip3 install llist
from pyllist import sllist

class Queue:
   def __init__(self):
      self.data=sllist()

   def enqueue(self,value):
      self.data.append(value)

