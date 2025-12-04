#Queue

'''
1.Linear Data Structure
2.Follows FIFO First in first out
3.Insertion can take place from Rear end
4.Insertion can take place from front end
5.Major operations:
   a.enqueue(ele) -   used to insert element at top
   b.dequeue()    -   removes the top element from queue
   c.peekfirst()  -   to get the first element of queue
   d.peeklast()   -   to get the last element of queue

6. All operation workd in constant time  i.e.. O(1)

'''

#Queue Implementation
'''
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) <1:
            return None
        return self.queue.pop(0)
    
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)
    

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.display()

q.dequeue()
print("After removing an element")
q.display()

'''

#Circular Queue implementation
#The last position is connected back to the first position (forms a circle 🔄)
#This allows efficient use of space — no wasted memory when elements are dequeued.

'''
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    # Enqueue operation
    def enqueue(self, value):
        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full 🚫")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

    # Dequeue operation
    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty ❌")
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    # Display queue
    
    def display(self):
        if self.front == -1:
            print("Queue is Empty ❌")
        elif self.rear >= self.front:
            print("Queue elements:", self.queue[self.front:self.rear + 1])
        else:
            print("Queue elements:", self.queue[self.front:] + self.queue[:self.rear + 1])

            
# Example usage

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.display()
cq.dequeue()
cq.enqueue(50)
cq.display()

'''
































