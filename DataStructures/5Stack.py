#Stack

'''
1.Linear data structure
2.It follows Last-in-first-out order
3.Insertion and removal of the element has done at one end
4.push is used for insertion of the element in a stack
5.pop is used for remove an element in a stack

'''
#Functions

'''
1.Push()
2.Pop()
3.size()
4.top()
5.empty()

'''
#Implementation using List

'''
stack = []
stack.append("abc")
print(stack)
stack.pop()
print(stack)

'''

#Implementation using collection deque
'''
from collections import deque

stack =deque()
stack.append("K")
print(stack)
stack.append("M")
stack.append("Y")

print(stack)

'''
#Implementation using queue
'''
from queue import LifoQueue
stack = LifoQueue()
stack.put(2)
stack.put(3)
stack.put(4)
print(stack.qsize())
print(stack.full())
stack.get()
print(stack.full())

'''





































