'''
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 


'''

class Node:

    def __init__(self, value):
        self.value = value
        self.next, self.prev = None, None

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.capacity = k
        self.size = 0
    

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        node = Node(value)
        if self.size == 0:
            self.head = self.tail = node
            node.next = node.prev = node
        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = self.head
            self.head.prev = node
            self.tail = node
        self.size += 1
        return True
    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        self.size -= 1
        return True


    def Front(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.head.value

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.tail.value

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        
        if self.size == self.capacity:
            return True
        else:
            return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
